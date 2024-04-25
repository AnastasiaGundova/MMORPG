from django.contrib import admin
from .models import Category, Author, Post, Reply, Image, Video, File

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Image)
admin.site.register(Video)
admin.site.register(File)
admin.site.register(Reply)
