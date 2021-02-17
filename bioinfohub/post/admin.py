from django.contrib import admin
from .models import *


# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'slug', 'author', 'created_at', 'can_comment')
	list_display_links = ('id', 'title')
	list_filter = ('title', 'author', 'created_at')
	search_fields = ('title', 'author', 'content', 'description')
	list_per_page = 25

class CommentAdmin(admin.ModelAdmin):
	list_display = ('id', 'comment', 'post_id', 'author', 'comment_date')
	list_display_links = ('id', 'comment')
	list_filter = ('comment', 'author', 'post_id')
	list_per_page = 25
	search_fields = ('comment', 'author', 'post_id')

class SavedPostAdmin(admin.ModelAdmin):
	list_display = ('id', 'post', 'user', 'save_date')
	list_display_links = ('id', 'post')
	list_filter = ('post', 'user')
	list_per_page = 25
	search_fields = ('user', 'post')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(SavedPost, SavedPostAdmin)


