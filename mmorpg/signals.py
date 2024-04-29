from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string

from MMORPG_project import settings
from mmorpg.models import PostCategory, Reply, Post
from django.db.models.signals import post_save
# from mmorpg.tasks import reply_accepted_send_email


def send_notifications(preview, pk, title, subscribers):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/posts/{pk}'
        }
    )
    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@receiver(m2m_changed, sender=PostCategory)
def notification_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        subscribers_emails = []

        for cat in categories:
            subscribers = cat.subscribers.all()
            subscribers_emails += [s.email for s in subscribers]

        send_notifications(instance.preview(), instance.pk, instance.title, subscribers_emails)


@receiver(post_save, sender=Reply)
def reply_accepted_notification(sender, instance, created, **kwargs):
    if not created and instance.is_accepted:
        html_content = render_to_string(
            'reply_accepted_email.html',
            {
                'instance': instance,
                'link': f'{settings.SITE_URL}/posts/reply/{instance.pk}'
            }
        )
        msg = EmailMultiAlternatives(
            subject=f'Отклик принят - {instance.text}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[instance.user.email],
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()


@receiver(post_save, sender=Reply)
def notification_about_reply(sender, instance, created, **kwargs):
    if created:
        html_content = render_to_string(
            'reply_created_email.html',
            {
                'instance': instance,
                'link': f'{settings.SITE_URL}/posts/reply/{instance.pk}'
            }
        )

        msg = EmailMultiAlternatives(
            subject=f'Отклик на объявление - {instance.text}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[instance.post.author.user.email],
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()

