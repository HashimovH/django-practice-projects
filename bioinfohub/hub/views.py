from django.shortcuts import render
from post.models import *
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from account.models import Profile
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
def index(request):
	posts = Post.objects.order_by('-created_at').filter(status='Published')
	# about_us = AboutSite.objects.get(id=1)
	paginator = Paginator(posts, 9)
	page = request.GET.get('page')
	post_listings = paginator.get_page(page)
	context = {
		'posts': post_listings,
		# 'about': about_us
	}
	return render(request, 'hub/index.html', context)

def about(request):
	about_us = get_object_or_404(AboutSite,id=1)
	context = {
		'about': about_us
	}
	return render(request, 'hub/about.html', context)


def authors(request):
	profiles = Profile.objects.all()
	context = {
		'profiles': profiles
	}
	return render(request, 'hub/authors.html', context)


def authorDetail(request, pk):
	author = User.objects.get(username=pk)
	profile = Profile.objects.get(user=author)
	posts = Post.objects.order_by('-created_at').filter(status='Published', author=author)
	paginator = Paginator(posts, 6)
	page = request.GET.get('page')
	posts_paginated = paginator.get_page(page)
	context = {
		'author': profile,
		'posts': posts_paginated
	}
	return render(request, 'hub/authorDetail.html', context)


# def search(request):
# 	queryset_list = Post.objects.order_by('-created_at')

# 	if 'q' in request.GET:
# 		query = request.GET['q']
# 		if query:
# 			queryset_list = queryset_list.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(content__icontains=query))

# 	paginator = Paginator(queryset_list, 1)
# 	page = request.GET.get('page')
# 	paginated_result = paginator.get_page(page)
# 	context = {
# 		'posts': paginated_result
# 	}
# 	return render(request, 'hub/search.html', context)