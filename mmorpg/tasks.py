from celery import shared_task
from django.core.mail import send_mail

from MMORPG_project import settings
from mmorpg.models import Reply

#
# @shared_task
# def reply_send_email(reply_id):
#     reply = Reply.objects.get(id=reply_id)
#     send_mail(
#         subject=f'Новый отклик на объявление!',
#         message=f'{reply.reply.user}, ! На ваше объявление есть новый отклик!\n'
#                 f'Прочитать отклик:\nhttp://127.0.0.1:8000/posts/{reply.post.id}',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         recipient_list=[reply.post.author.user.email, ],
#     )
#
#
# @shared_task
# def reply_accepted_send_email(reply_id):
#     reply = Reply.objects.get(id=reply_id)
#     send_mail(
#         subject=f'Ваш отклик принят!',
#         message=f'{reply.reply.user}, aвтор объявления {reply.post.title} принял Ваш отклик!\n',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         recipient_list=[reply.post.author.user.email, ],
#     )
