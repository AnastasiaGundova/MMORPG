from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, TemplateView

from sign.views import ConfirmUser, BaseRegisterView

urlpatterns = [
    path('login/',
         LoginView.as_view(template_name='sign/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name='sign/logout.html'),
         name='logout'),
    path('logout/confirm/',
         TemplateView.as_view(template_name='logout_confirm.html'),
         name='logout_confirm'),
    path('index/',
         LoginView.as_view(template_name='protect/index.html'),
         name='index'),
    path('signup/', BaseRegisterView.as_view(template_name='sign/signup.html'), name='signup'),
    path('confirm/', ConfirmUser.as_view(), name='confirm_user')
]
