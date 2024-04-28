from django_filters import FilterSet

from mmorpg.models import Reply, Post


class RepliesFilter(FilterSet):
    class Meta:
        model = Reply
        fields = [
            'post'
        ]

    def __init__(self, *args, **kwargs):
        super(RepliesFilter, self).__init__(*args, **kwargs)
        self.filters['post'].queryset = Post.objects.filter(author__user_id=kwargs['request'])