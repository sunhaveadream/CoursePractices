from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost, BlogArtical
from .forms import BlogPostForm, BlogArticalForm

def index(request):
	"""博客的主页"""
	return render(request, 'learning_blogs/index.html')

@login_required
def blogposts(request):
	"""显示所有的博客"""
	blogposts = BlogPost.objects.filter(owner=request.user).order_by('date_added')
	context = {'blogposts': blogposts}
	return render(request, 'learning_blogs/blogposts.html', context)

@login_required
def blogpost(request, blogpost_id):
	"""显示单个博客及其所有的内容"""
	blogpost = BlogPost.objects.get(id=blogpost_id)
	if blogpost.owner != request.user:
		raise Http404

	blogarticals = blogpost.blogartical_set.order_by('-date_added')
	context = {'blogpost': blogpost, 'blogarticals': blogarticals}
	return render(request, 'learning_blogs/blogpost.html', context)

@login_required
def new_blogpost(request):
	"""添加新博客"""
	if request.method != 'POST':
		form = BlogPostForm()
	else:
		form = BlogPostForm(data=request.POST)
		if form.is_valid():
			new_blogpost = form.save(commit=False)
			new_blogpost.owner = request.user
			new_blogpost.save()
			return redirect('learning_blogs:blogposts')

	context = {'form': form}
	return render(request, 'learning_blogs/new_blogpost.html', context)

@login_required
def new_blogartical(request, blogpost_id):
	"""在特定的博客添加新博文"""
	blogpost = BlogPost.objects.get(id=blogpost_id)
    
	if request.method != 'POST':
		form = BlogArticalForm()
	else:
		form = BlogArticalForm(data=request.POST)
		if form.is_valid():
			new_blogartical = form.save(commit=False)
			new_blogartical.blogpost = blogpost
			new_blogartical.save()
			return redirect('learning_blogs:blogpost', blogpost_id=blogpost_id)

	context = {'blogpost': blogpost, 'form': form}
	return render(request, 'learning_blogs/new_blogartical.html', context)

@login_required
def edit_blogartical(request, blogartical_id):
	"""编辑既有博文"""
	blogartical = BlogArtical.objects.get(id=blogartical_id)
	blogpost = blogartical.blogpost
	if blogpost.owner != request.user:
		raise Http404
    
	if request.method != 'POST':
		form = BlogArticalForm(instance=blogartical)
	else:
		form = BlogArticalForm(instance=blogartical, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('learning_blogs:blogpost', blogpost_id=blogpost.id)

	context = {'blogartical': blogartical, 'blogpost': blogpost, 'form': form}
	return render(request, 'learning_blogs/edit_blogartical.html', context)
	