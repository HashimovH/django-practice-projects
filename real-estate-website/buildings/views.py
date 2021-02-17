from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.utils.html import escape
from django.contrib import messages

from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.
def home(requests):
	# Global
	categories = Category.objects.all().order_by('-id')
	sm = SocialMedia.objects.all().order_by('-id')
	info = None
	try:
		info = Option.objects.get(id=1)
	except:
		print("Error")


	recent_listings = Estate.objects.all().order_by('-id')[:6]
	services = Service.objects.all().order_by('-id')
	is_featured = Estate.objects.all().filter(is_featured=False).order_by('-id')[:6]


	context = {
		'home': True,

		'categories': categories,
		'sm': sm,
		'info': info,
		'recent': recent_listings,
		'services': services,
		'is_featured': is_featured
	}
	return render(requests, "buildings/home.html", context)

def about(requests):
	info = None
	try:
		info = Option.objects.get(id=1)
	except:
		print("Error")
	categories = Category.objects.all().order_by('-id')
	sm = SocialMedia.objects.all().order_by('-id')



	statistics = Statistic.objects.all().order_by('-id')
	services = Service.objects.all().order_by('-id')
	teams = Team.objects.all().order_by()


	context = {
		'info': info,
		'statistics': statistics,
		'services': services,
		'teams': teams,
		'count_teams': teams.count(),
		'services_count': services.count(),
		'statistics_count': statistics.count(),
		'about': True,
		'categories': categories,
		'sm': sm
	}
	return render(requests, "buildings/about.html", context)

def contact(requests):
	info = None
	try:
		info = Option.objects.get(id=1)
	except:
		print("Error")

	categories = Category.objects.all().order_by('-id')
	sm = SocialMedia.objects.all().order_by('-id')

	context = {
		'info': info,
		'contact': True,
		'categories': categories,
		'sm': sm
	}
	return render(requests, "buildings/contact.html", context)


def estates(requests):
	# Global
	info = None
	cat = None
	beds = None
	try:
		info = Option.objects.get(id=1)
	except:
		print("Error")
	categories = Category.objects.all().order_by('-id')
	sm = SocialMedia.objects.all().order_by('-id')

	cats = Category.objects
	estates = Estate.objects.all()

	if requests.GET.get('cat'):
		slug = escape(requests.GET['cat'])
		cat = cats.get(slug=slug)
		estates = estates.filter(category=cat).order_by('-id')

	if requests.GET.get('bedrooms'):
		beds = escape(requests.GET.get('bedrooms'))
		estates = estates.filter(bedrooms=beds).order_by('-id')

	if requests.GET.get('type'):
		type_ = escape(requests.GET.get('type'))
		estates = estates.filter(pr_type=type_).order_by('-id')

	if requests.GET.get('utility'):
		utility = escape(requests.GET.get('utility'))
		estates = estates.filter(utility_included=utility).order_by('-id')

	if requests.GET.get('parking'):
		parking = escape(requests.GET.get('parking'))
		estates = estates.filter(has_parking=parking).order_by('-id')

	if requests.GET.get('transport'):
		transport = escape(requests.GET.get('transport'))
		estates = estates.filter(transportation=transport).order_by('-id')


	paginator = Paginator(estates, 15)
	page = requests.GET.get('page')
	estate_listings = paginator.get_page(page)

	# 3 new home
	recent_houses = Estate.objects.all().filter(status="publish").order_by('-id')[:3]

	context = {
		'estates': estate_listings,
		'categories': categories,
		'sm': sm,
		'info': info,
		'estates_menu': True,
		'recents': recent_houses,
		'cat': cat,

		'bedrooms': beds
	}
	return render(requests, "buildings/listings.html", context)

def detail(requests, pk):
	# Global
	info = None
	try:
		info = Option.objects.get(id=1)
	except:
		print("Error")
	categories = Category.objects.all().order_by('-id')
	sm = SocialMedia.objects.all().order_by('-id')

	estate = get_object_or_404(Estate, slug=pk)

	images = Image.objects.all().filter(estate=estate)
	amenities = AmenitiesAndEstates.objects.all().filter(estate=estate).order_by('-id')
	nearby = Nearby.objects.all().filter(estate=estate).order_by('-id')

	reviews = Review.objects.all().filter(estate=estate).order_by('-id')
	review_count = reviews.count()


	# 3 new home
	recent_houses = Estate.objects.all().filter(status="publish").order_by('-id')[:3]

	context = {
		'categories': categories,
		'sm': sm,
		'info': info,
		'estates_menu': True,
		'estate': estate,
		'images': images,
		'amenities': amenities,
		'nearby': nearby,
		'reviews': reviews,
		'r_count': review_count,
		'recents': recent_houses,
		'message_form': MessageForm
	}
	return render(requests, "buildings/detail.html", context)


def submitReview(requests):
	full_name = escape(requests.POST['name'])
	review = escape(requests.POST['review'])
	estate = escape(requests.POST['estate'])
	email = escape(requests.POST['email'])
	rating = escape(requests.POST['rating'])

	estate = get_object_or_404(Estate, id=estate)

	new_review = Review(full_name=full_name, email=email, description=review, estate=estate, rating=rating)

	try:
		new_review.save()
		messages.success(requests, "Your review has been submitted successfully.")
	except Exception as e:
		messages.warning(requests, "Your review cannot submitted.")


	return redirect('detail', estate.slug)


def submitRequest(requests, estate):
	estate = get_object_or_404(Estate, id=estate)

	new_request = MessageForm(requests.POST)
	if new_request.is_valid():
		try:
			new_request.save(commit=False)
			new_request.estate = estate
			new_request.save()
			messages.success(requests, "Your request has been submitted successfully.")
		except Exception as e:
			messages.warning(requests, "Your requests can not submitted.")
	else:
		messages.warning(requests, "Please, enter valid data.")

	return redirect('detail', estate.slug)

# def search(requests):
# 	context = {}
# 	return render(requests, "buildings/home.html", context)