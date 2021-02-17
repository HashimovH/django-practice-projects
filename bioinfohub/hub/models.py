from django.db import models

# Create your models here.
class AboutSite(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=150)
	about_us = models.TextField()
	email = models.CharField(max_length=155)
	phone = models.CharField(max_length=155)