from ckeditor.fields import RichTextFormField, RichTextField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import Post, Reply, Author

from allauth.account.forms import SignupForm
from django.core.mail import send_mail
from random import sample
from string import hexdigits
from django.conf import settings


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'text',
            'category',
        ]

        def clean(self):
            cleaned_data = super().clean()
            title = cleaned_data.get("title")
            text = cleaned_data.get("text")

            if title == text:
                raise ValidationError(
                    "The title cannot be identical to the content"
                )

            return cleaned_data


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = [
            'text',
        ]

        def clean(self):
            cleaned_data = super().clean()
            return cleaned_data


class CommonSignupForm(SignupForm):
    def save(self, request):
        user = super(CommonSignupForm, self).save(request)
        user.is_active = False
        code = ''.join(sample(hexdigits, 5))
        user.code = code
        user.save()
        Author.objects.create(user=user, code=code)
        send_mail(
            subject='Код',
            message=f'Ваш код активации {code}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email]
        )
        return user
