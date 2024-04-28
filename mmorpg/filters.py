from django.forms import DateInput
from django_filters import FilterSet, DateFilter, ModelChoiceFilter, CharFilter
from .models import Author


class PostFilter(FilterSet):

    title = CharFilter(
        label='Heading',
        lookup_expr='iregex'
    )

    author = ModelChoiceFilter(
        empty_label='All authors',
        label='User',
        queryset=Author.objects.all()
    )

    created_at = DateFilter(
        field_name='created_at',
        widget=DateInput(attrs={'type': 'date'}),
        lookup_expr='date__gte',
        label='Date'
    )


class ReplyFilter(FilterSet):
    title = CharFilter(
        field_name='text',
        label='Heading',
        lookup_expr='iregex'
    )
