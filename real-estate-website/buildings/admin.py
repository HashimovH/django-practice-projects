from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Estate)
# admin.site.register(Image)
# admin.site.register(Extra)
# admin.site.register(ExtraEstate)
# admin.site.register(Message)

class CatAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'slug')
	list_display_links = ('id', 'title')
	list_per_page = 20


admin.site.register(Category, CatAdmin)


# Options
admin.site.register(Option)
# Social Media
admin.site.register(SocialMedia)
# Amenities
admin.site.register(Amenities)

class EstateImageAdmin(admin.StackedInline):
    model = Image


class EstateAmenityAdmin(admin.StackedInline):
    model = AmenitiesAndEstates


class NearbyAdmin(admin.StackedInline):
    model = Nearby
 
@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
	inlines = [EstateImageAdmin, EstateAmenityAdmin, NearbyAdmin]
	list_display = ('id', 'title', 'status', 'category', 'is_featured')
	list_display_links = ('id', 'title')
	list_filter = ('category', 'is_featured', 'status')
	search_fields = ('title', 'author', 'content', 'description')
	list_per_page = 25

	class Meta:
	   model = Estate
 
@admin.register(Image)
class PostImageAdmin(admin.ModelAdmin):
    pass



# About us Models
class ServiceAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'description')
	list_display_links = ('id', 'title')
	list_per_page = 20

class StatisticAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'count')
	list_display_links = ('id', 'title')
	list_per_page = 20


class TeamAdmin(admin.ModelAdmin):
	list_display = ('id', 'full_name', 'title')
	list_display_links = ('id', 'title')
	list_per_page = 20



admin.site.register(Service, ServiceAdmin)
admin.site.register(Statistic, StatisticAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Message)


