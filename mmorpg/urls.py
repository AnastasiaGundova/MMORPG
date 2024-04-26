from django.urls import path
from .views import PostsList, PostSearch, PostDetail


urlpatterns = [
   path('', PostsList.as_view(), name='posts_list'),
   path('posts/<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('search/', PostSearch.as_view(), name='post_search'),
]