from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm
from .models import Post, Category
from .filters import PostFilter

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.core.cache import cache

from django.utils import timezone

from django.shortcuts import redirect

import pytz

from django.utils.translation import gettext as _


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
        context['current_time'] = timezone.localtime(timezone.now())
        context['timezones'] = pytz.common_timezones
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
        context['current_time'] = timezone.localtime(timezone.now())
        context['timezones'] = pytz.common_timezones
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


class PostCreate(PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'managing_posts/post_create.html'
    success_url = '/home/news'
    permission_required = ('news.add_post',)

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == '/home/articles/create/':
            post.type = 'A'
        elif self.request.path == '/home/news/create/':
            post.type = 'N'

        post.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProtectedView(TemplateView):
    template_name = 'prodected_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_time'] = timezone.localtime(timezone.now())
        context['timezones'] = pytz.common_timezones
        return context

