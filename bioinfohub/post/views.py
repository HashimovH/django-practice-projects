from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from account.models import Profile
from django.contrib.auth.decorators import login_required #login required decorator
from django.contrib import messages, auth #Messages
from django.utils.text import slugify
import datetime



# Create your views here.

@login_required
def createPost(request):
	if request.method == 'GET':
		form = PostForm()
		context = {
			'form': form
		}
		return render(request, 'post/create.html', context)
	elif request.method == 'POST':
		try:
			form = PostForm(request.POST, request.FILES)
			new_post = form.save(commit=False)
			new_post.author = request.user
			slug_for_store = form.cleaned_data.get('title') + '-' + str(datetime.datetime.now())
			new_post.slug = slugify(slug_for_store)
			new_post.save()
			messages.success(request, 'Your post has been created.')
		except ValueError:
			context = {
				'form': form,
				'error': 'Data is not valid.'
			}
			return render(request, 'post/create.html', context)
		return redirect('/')

def postDetail(request, pk):
	post = get_object_or_404(Post, slug=pk, status='Published')
	author_profile = Profile.objects.get(user=post.author)
	extra_posts = Post.objects.order_by('-created_at')[:3]
	comments = Comment.objects.order_by('-comment_date').filter(post_id=post)
	post.preview = post.preview + 1
	post.save()

	if request.user.is_authenticated:
		is_saved = SavedPost.objects.all().filter(user=request.user, post=post).count()
	else:
		is_saved = 1

	save_count = SavedPost.objects.all().filter(post=post).count()


	if is_saved >= 1:
		is_saved = True
	else:
		is_saved = False

	#Comment Form
	comment_form = CommentForm()
	context = {
		'post': post,
		'author': author_profile,
		'extra': extra_posts,
		'comment_form': comment_form,
		'comments': comments,
		'is_saved': is_saved,
		'save_count': save_count
	}

	#if comment form submitted
	if request.method == 'POST':
		new_comment_form = CommentForm(request.POST)
		try:
			new_comment_form = new_comment_form.save(commit=False)
			new_comment_form.author = request.user
			new_comment_form.post_id = post
			new_comment_form.save()
		except ValueError:
			context.update({ 'error': 'Data is not valid.' })

	return render(request, 'post/detail.html', context)


@login_required
def postEdit(request, pk):
	post = Post.objects.get(id=pk)
	form = PostForm(instance=post)
	context = {
		'form': form
	}

	if request.method == 'POST':
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			try:
				form.save()
				messages.success(request, "Post has been updated!")
				return redirect('/profile')
			except ValueError:
				context+={
					'error': 'Data is not valid!'
				}

	return render(request, 'post/edit.html', context)



@login_required
def postDelete(request, pk):
	post = get_object_or_404(Post, id=pk)
	context = {
		'post': post
	}

	if request.method == 'POST':
		post.delete()
		return redirect('/profile')
	return render(request, 'post/delete.html', context)



@login_required
def postSave(request, pk):
	post = get_object_or_404(Post, id=pk)
	user = request.user

	save_post = SavedPost.objects.create(post=post, user=user)
	save_post.save()
	return redirect('post-detail', pk=post.slug)

def postSaveDelete(request, pk):
	if request.method == 'POST':
		save = get_object_or_404(SavedPost, id=pk)
		save.delete()
		return redirect('/profile')

