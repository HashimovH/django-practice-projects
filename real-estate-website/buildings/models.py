from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
	title = models.CharField(max_length=244)
	slug = models.SlugField(null=True)

	def __str__(self):
		return self.title

class Estate(models.Model):

	STATUS_TYPE = (
		('draft', 'Draft'),
		('publish', 'Published')
	)

	pr_types = (
		('house', 'House'),
		('apartment', 'Apartment'),
	)

	YES_NO = (
		('yes', 'Yes'),
		('no', 'No')
	)

	FAR_CLOSE = (
		('far', 'Far'),
		('close', 'Close')
	)

	title = models.CharField(max_length=255)
	description = RichTextField()
	pr_type = models.CharField(max_length=20, choices=pr_types)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	rooms = models.IntegerField()
	bedrooms = models.IntegerField()
	bath = models.IntegerField()
	plan_1 = models.ImageField(upload_to="estate/%Y/%m/%d", null=True, blank=True)
	video_url = models.URLField(null=True, blank=True)
	video_cover = models.ImageField(upload_to="estate/%Y/%m/%d", null=True, blank=True)
	address = models.CharField(max_length=255, null=True, blank=True)
	is_featured = models.BooleanField(default=False, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=10, choices=STATUS_TYPE)
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
	image_main = models.ImageField(upload_to="estate/%Y/%m/%d", null=True)
	slug = models.SlugField(null=True)

	utility_included = models.CharField(max_length=3, choices=YES_NO, null=True)
	has_parking = models.CharField(max_length=3, choices=YES_NO, null=True)
	transportation = models.CharField(max_length=6, choices=FAR_CLOSE, null=True)
	
	def __str__(self):
		return self.title

class Nearby(models.Model):
	TYPES = (
		('blue', 'Education'),
		('green', 'Health&Medical'),
		('red', 'Transportation')
	)

	title = models.CharField(max_length=255)
	distance = models.CharField(max_length=255)
	type_of = models.CharField(max_length=100, choices=TYPES)
	estate = models.ForeignKey(Estate, on_delete=models.CASCADE, null=True)


class Amenities(models.Model):
	title = models.CharField(max_length=255)

	def __str__(self):
		return self.title


class AmenitiesAndEstates(models.Model):
	amenity = models.ForeignKey(Amenities, on_delete=models.CASCADE)
	estate = models.ForeignKey(Estate, on_delete=models.CASCADE)

class Image(models.Model):
	image = models.ImageField(upload_to="images/estate/%Y/%m/%d")
	estate = models.ForeignKey(Estate, on_delete=models.CASCADE)

class Extra(models.Model):
	title = models.CharField(max_length=255)

class ExtraEstate(models.Model):
	extra = models.ForeignKey(Extra, on_delete=models.SET_NULL, null=True, blank=True)
	estate = models.ForeignKey(Estate, on_delete=models.SET_NULL, null=True, blank=True)


class Review(models.Model):
	full_name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	description = models.CharField(max_length=255)
	rating = models.IntegerField()
	estate = models.ForeignKey(Estate, on_delete=models.CASCADE, null=True, blank=True)
	email = models.EmailField(null=True)

class Message(models.Model):
	full_name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	phone = models.CharField(max_length=25)
	message = models.TextField()
	estate = models.ForeignKey(Estate, on_delete=models.CASCADE, null=True, blank=True)
	message_date = models.DateTimeField(auto_now_add=True)


class Option(models.Model):
	phone = models.CharField(max_length=25)
	email = models.EmailField()
	logo = models.ImageField(upload_to="images/")
	address = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	company_name = models.CharField(max_length=255, null=True, blank=True)
	about_us = RichTextField(null=True, blank=True)

	def __str__(self):
		return self.company_name

class Service(models.Model):
	title = models.CharField(max_length=255)
	icon = models.ImageField(upload_to="images/service/")
	description = models.CharField(max_length=255)

class Statistic(models.Model):
	title = models.CharField(max_length=60)
	icon = models.CharField(max_length=50)
	count = models.IntegerField()

class Team(models.Model):
	full_name = models.CharField(max_length=50)
	image = models.ImageField(upload_to="images/team/")
	facebook = models.URLField()
	linkedin = models.URLField()
	website = models.URLField()
	title = models.CharField(max_length=50)


class SocialMedia(models.Model):
	title = models.CharField(max_length=100)
	url = models.URLField()

	def __str__(self):
		return self.title