from django.shortcuts import render
from django.forms import inlineformset_factory
from .forms import PostForm
from .models import Post, Media


def post_media_form(request):

    PostMediaFormSet = inlineformset_factory(Post, Media, form=PostForm, extra=1)
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        formset = PostMediaFormSet(request.POST, instance=Post())
        if post_form.is_valid() and formset.is_valid():
            post = post_form.save()
            formset.instance = post
            formset.save()
    else:
        post_form = PostForm()
        formset = PostMediaFormSet(instance=Post())
    return render(request, 'post_list.html', {'post_form': post_form, 'formset': formset})
