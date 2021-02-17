#Pagination imports
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
#=======================================================================|
#Models import
from post.models import Post, SavedPost
from .models import Profile 
from django.contrib.auth.models import User #User model
#=======================================================================|
#my forms import
from .forms import ProfileForm
#=======================================================================|
#authentication imports
from django.contrib.auth.forms import UserCreationForm # Registration form
from django.contrib.auth import login as login_user, logout, authenticate #Login Logout functions
from django.contrib.auth.decorators import login_required #login required decorator
#=======================================================================|
from django.shortcuts import render, redirect, get_object_or_404 #import render redirect and Get object
from django.db import IntegrityError # Exception error
from django.contrib import messages, auth #Messages
from django.http import HttpResponse
#Email imports

#=======================================================================|
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string

#Verification imports
#=======================================================================|
import hashlib


def register(request):
	form = UserCreationForm()
	if request.method == 'GET':
		context = {
			'form': form
		}
		return render(request, 'account/register.html', context)
	else:
		name = request.POST['name']
		surname = request.POST['surname']
		email = request.POST['email']
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		if(password1 == password2):
			if len(password1) > 6:
				try:
					is_exists = User.objects.all().filter(email=email).count()
					if is_exists >= 1:
						context = {
							'form': form,
							'error': 'This email has already been taken. Please choose another email.'
						}
						return render(request, 'account/register.html', context)
					user = User.objects.create_user(username, email=email,password=password1, first_name=name, last_name=surname)
					user.save()
					#Send Email
					hashing_info = hashlib.sha256("{}".format(email).encode('utf-8')).hexdigest()
					profile = get_object_or_404(Profile, user=user)
					profile.activate_hash = hashing_info
					profile.save()
					link = '{}activate/{}/'.format(request.build_absolute_uri()[:-9], hashing_info)
					mail_subject = "Please activate your account"
					to_email = email
					message = render_to_string('account/acc_active_email.html', {
					    'user':user,
					    'url': link,
					    'email': to_email
					})
					email = EmailMessage(
					    mail_subject, message,from_email='dnaworldosc@gmail.com', to=[to_email]
					)
					email.send(fail_silently=True)
					return render(request, 'account/confirm_email.html')
				except IntegrityError:
					context = {
						'form': form,
						'error': 'The username has already been taken. Please choose another username.'
					}
					return render(request, 'account/register.html', context)
			else:
				context = {
					'form': form,
					'error': 'Password must be longer than 6 characters!'
				}
				return render(request, 'account/register.html', context)
		else:
			context = {
				'form': form,
				'error': 'Passwords do not match!'
			}
			return render(request, 'account/register.html', context)

def activate(request, pk):
	if request.method == 'GET':
		profile = get_object_or_404(Profile,activate_hash=pk)
		if profile:
			profile.email_confirmed = True
			profile.save()
			profile.activate_hash = ''
			profile.save()
			return redirect('/login')
		else:
			return HttpResponse('The profile is missing')
	else:
		return HttpResponse('This url is not valid!')


def login(request):
	if request.method == 'GET':
		return render(request, 'account/login.html')
	else:
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user:
			profile = Profile.objects.get(user=user)
		if user is None:
			return render(request, 'account/login.html', {'error': 'Username or password did not match.'})
		elif profile.email_confirmed == False:
			return render(request, 'account/login.html', {'error': 'Account must be activated.'})
		else:
			login_user(request, user)
			messages.success(request, "You are successfully logged in.")
			return redirect('/')


@login_required
def profile(request):
	user = get_object_or_404(User,username=request.user)
	profile = Profile.objects.get(user=user)
	form = ProfileForm(instance=profile)

	my_posts = Post.objects.order_by('-created_at').filter(author=user)
	paginator = Paginator(my_posts, 25)
	page = request.GET.get('page')
	posts_paginated = paginator.get_page(page)


	my_saved_posts = SavedPost.objects.order_by('-save_date').filter(user=request.user)
	spaginator = Paginator(my_saved_posts, 25)
	spage = request.GET.get('spage')
	saved_paginated = spaginator.get_page(spage)


	context = {
		'user': user,
		'profile': profile,
		'form': form,
		'my_posts': posts_paginated,
		'saved_posts': saved_paginated
	}

	return render(request, 'account/myProfile.html', context)

@login_required
def updateProfile(request):
	user = get_object_or_404(User,username=request.user)
	profile = Profile.objects.get(user=user)
	profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
	if profile_form.is_valid():
		try:
			profile_form.save()
			return redirect('/profile')
		except ValueError: 
			context += {
				'error': 'Data is not valid!'
			}
			return redirect('/profile')


@login_required
def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		messages.success(request, 'You are now logged out.')
		return redirect('index')

