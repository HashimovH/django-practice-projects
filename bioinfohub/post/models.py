from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):

	STATUS = (
		('Published', 'Published'),
		('Drafted', 'Drafted'),
		('Deleted', 'Deleted')
	)

	title = models.CharField(max_length=100)
	description = models.CharField(max_length=200)
	content = models.TextField()
	slug = models.SlugField(max_length=150, unique=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	status = models.CharField(max_length=50, choices=STATUS)
	preview = models.IntegerField(default=0, null=True, blank=True)
	image = models.ImageField(upload_to='photos/%Y/%m/%d/')
	can_comment = models.BooleanField(default=True)

	def __str__(self):
		return self.title


class Comment(models.Model):
	comment = models.TextField()
	post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	comment_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	is_reply = models.BooleanField(default=False)


class SavedPost(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	save_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)