from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=15, blank=True, null=True)


class Category(models.Model):
    subscribers = models.ManyToManyField(User, blank=True, null=True, related_name='categories')
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')

    def __str__(self):
        return self.title

    def preview(self):
        return self.text[:125].strip() + "..."

    def __str__(self):
        return f'id - {self.pk}: {self.title}'

    def get_absolute_url(self):
        return f'/posts/{self.id}'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


# class Image(models.Model):
#     data = models.CharField(max_length=2083)
#     title = models.CharField(max_length=255, verbose_name='заголовок')
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
#
#     def __str__(self):
#         return f'{self.pk} {self.title}'


class Media(models.Model):

    Image = 'IM'
    Video = 'VD'
    Audio = 'AU'
    File = 'FL'

    MEDIA_CHOICES = (
        ('IM', 'Image'),
        ('VD', 'Video'),
        ('AU', 'Audio'),
        ('FL', 'File'),
    )

    type = models.CharField(max_length=2, choices=MEDIA_CHOICES)
    data = models.CharField(max_length=2083)
    title = models.CharField(max_length=255, verbose_name='заголовок')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='media')

    def __str__(self):
        return f'{self.pk} {self.title}'


# class Video(models.Model):
#     data = models.CharField(max_length=2083)
#     title = models.CharField(max_length=255, verbose_name='заголовок')
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='videos')
#
#     def __str__(self):
#         return f'{self.pk} {self.title}'


# class File(models.Model):
#     title = models.CharField(max_length=255)
#     file = models.FileField(upload_to='files/', blank=True, null=True)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='files')
#
#     def __str__(self):
#         return f'{self.pk} {self.title}'


class Reply(models.Model):
    reply_text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
