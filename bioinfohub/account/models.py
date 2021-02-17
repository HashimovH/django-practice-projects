from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	avatar = models.ImageField(upload_to='photos/%y/%m/%d/', default='default.jpg')
	about = models.CharField(max_length=150, blank=True, null=True)
	bio = models.CharField(max_length=50, blank=True, null=True)
	facebook = models.URLField(blank=True, null=True)
	linkedin = models.URLField(blank=True, null=True)
	goodwall = models.URLField(blank=True, null=True)
	twitter = models.URLField(blank=True, null=True)
	website = models.URLField(blank=True, null=True)
	email_confirmed = models.BooleanField(default=False, blank=True, null=True)
	activate_hash = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return f'{self.user.username} Profile'