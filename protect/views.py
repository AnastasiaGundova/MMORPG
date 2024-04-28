from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from mmorpg.models import Reply
from protect.filter import RepliesFilter


class IndexView(LoginRequiredMixin, ListView):
    model = Reply
    template_name = 'protect/index.html'
    context_object_name = 'post_reply'

    def get_queryset(self):
        queryset = Reply.objects.filter(post__author__user_id=self.request.user.id)
        self.filterset = RepliesFilter(self.request.GET, queryset, request=self.request.user.id)
        if self.request.GET:
            return self.filterset.qs
        return Reply.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context
