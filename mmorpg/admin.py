from django.contrib import admin
from .models import Category, Author, Post, Reply, PostCategory


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = 'title'
    list_filter = ('created_at', 'title')
    search_fields = ('title', 'category')


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    search_fields = ['name']


admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Reply)
