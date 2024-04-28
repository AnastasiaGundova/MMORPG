from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from MMORPG_project.settings import SITE_URL
from .forms import PostForm, ReplyForm
from .models import Post, Category, Reply
from .filters import PostFilter

from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.cache import cache


class PostsList(ListView):
    model = Post
    template_name = 'pages/posts_list.html'
    context_object_name = 'posts'
    ordering = '-created_at'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'pages/post_detail.html'
    context_object_name = 'post'

    def get_object(self, *args, **kwargs):
        obj = cache.get(f'post-{self.kwargs["pk"]}', None)

        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'post-{self.kwargs["pk"]}', obj)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostSearch(ListView):
    model = Post
    ordering = 'title'
    template_name = 'pages/post_search.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostCreate(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'managing_posts/post_create.html'
    success_url = ''

    def form_valid(self, form):
        post = form.save(commit=True)
        post.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'managing_posts/post_edit.html'
    success_url = ''


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'managing_posts/post_delete.html'
    success_url = 'http://127.0.0.1:8000/posts/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CategoryListView(PostsList):
    model = Post
    template_name = 'category_list.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(category=self.category).order_by('created_at')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscribed'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context


class ReplyDetailView(DetailView):
    model = Reply
    template_name = 'pages/reply_detail.html'
    context_object_name = 'reply_detail'


class ReplyDelete(LoginRequiredMixin, DeleteView):
    model = Reply
    template_name = 'managing_posts/reply_delete.html'
    success_url = 'http://127.0.0.1:8000/posts/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ReplyCreate(LoginRequiredMixin, CreateView):
    form_class = ReplyForm
    model = Reply
    template_name = 'managing_posts/reply_create.html'
    context_object_name = 'reply_create'
    success_url = SITE_URL + '/posts/'

    def form_valid(self, form):
        post_id = self.kwargs.get('pk')
        post = get_object_or_404(Post, pk=post_id)

        reply = form.save(commit=False)
        reply.post = post
        reply.user = self.request.user
        reply.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@login_required()
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)

    message = 'Вы подписались на категорию'

    return render(request, 'subscribe.html', {category: category, 'message': message})
