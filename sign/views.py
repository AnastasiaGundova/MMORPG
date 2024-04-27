from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView

from .models import BaseRegisterForm
from mmorpg.models import Author


class BaseRegisterView(CreateView):
    model = Author
    form_class = BaseRegisterForm
    success_url = '/confirm/'


class ConfirmUser(UpdateView):
    model = Author
    context_object_name = 'confirm_user'

    def post(self,  request, *args, **kwargs):
        if 'code' in request.POST:
            code = request.POST['code']
            user = Author.objects.filter(code=code)
            if user.exists():
                user = user.first()  # Получаем первого пользователя с указанным кодом
                user.is_active = True
                user.code = None  # Очищаем код после активации
                user.save()  # Сохраняем изменения в экземпляре пользователя
            else:
                return render(request, 'sign/invalid_code.html')
            return redirect('/')
