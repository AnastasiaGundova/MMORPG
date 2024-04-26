from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView

from mmorpg.forms import CommonSignupForm
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
            user = Author.objects.filter(code=request.POST['code'])
            if user.exists():
                user.update(is_active=True)
                user.update(code=None)
            else:
                return render(self.request, 'sign/registration_code.html')
            return redirect('/')