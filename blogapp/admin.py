from django.contrib import admin
from .models import Category, Post, Comment, Email
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','category')
    list_filter = ('category', 'created')
    search_fields = ('title','body')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created','active')
    list_filter = ('created', 'active')
    search_fields = ('name', 'email', 'body')

class EmailAdmin(admin.ModelAdmin):
    list_display = ('name', 'email_address')
    list_filter = ('time',)


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Email, EmailAdmin)