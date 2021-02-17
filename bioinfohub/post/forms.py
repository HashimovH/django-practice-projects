from django.forms import ModelForm
from .models import Post, Comment

class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'description', 'content', 'status', 'image', 'can_comment']


class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['comment']