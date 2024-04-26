from django.urls import path
from .views import PostsList, PostSearch, PostDetail, PostCreate, CategoryListView, subscribe, PostUpdate, PostDelete

urlpatterns = [
   path('', PostsList.as_view(), name='posts_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('search/', PostSearch.as_view(), name='post_search'),

   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),

   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
]
