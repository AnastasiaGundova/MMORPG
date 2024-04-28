from django.urls import path
from .views import PostsList, PostSearch, PostDetail, PostCreate, CategoryListView, subscribe, PostUpdate, PostDelete, \
   ReplyDetailView, ReplyCreate, ReplyDelete, ReplyEdit, reply_accept

urlpatterns = [
   path('', PostsList.as_view(), name='posts_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('search/', PostSearch.as_view(), name='post_search'),

   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),

   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),

   path('reply/<int:pk>/', ReplyDetailView.as_view(), name='reply_detail'),
   path('<int:pk>/reply/', ReplyCreate.as_view(), name='reply_create'),
   path('reply/<int:pk>/reply_delete/', ReplyDelete.as_view(), name='reply_delete'),
   path('reply/<int:pk>/reply_edit/', ReplyEdit.as_view(), name='reply_edit'),
   path('reply/<int:pk>/reply_accept/', reply_accept, name='reply_accept'),
]
