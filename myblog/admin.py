from django.contrib import admin
from myblog.models import *
# Register your models here.
class PostAdminPage(admin.ModelAdmin):
    list_display = ['title','createDate']
    ordering = ['createDate']
    search_fields = ['title']
	
class CommentAdminPage(admin.ModelAdmin):
    list_display = ['content','createDate','parentPost']
    ordering = ['createDate']
    # will be edited search_fields = ['user']
	

admin.site.register(Post, PostAdminPage)
admin.site.register(Comment, CommentAdminPage)