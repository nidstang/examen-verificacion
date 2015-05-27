# Create your views here.
from django.shortcuts import render_to_response, render
from .models import Post, PostForm
from django.template import Context
from django.template import RequestContext
from blog.util import Util

def home(request):
	return render_to_response("home.html", {})

def create_post(request):
	if request.method == "POST":
		postForm = PostForm(request.POST)

		if postForm.is_valid():
			title = postForm.cleaned_data['title']
			content = postForm.cleaned_data['content']

			new_post = Post.objects.create_post(title, content)
			new_post_form = PostForm()
			if new_post:
				return render(request, "create.html", {"post_form": new_post_form, 'success': True})
			else:
				return render(request, "create.html", {"post_form": new_post_form, 'error': True})
	else:
		postForm = PostForm()
		return render(request, "create.html", {"post_form": postForm})

def get_posts(request):
	posts = Post.objects.all()

	for post in posts:
		post.content = Util.string_to_upper(post.content)

	return render(request, "posts.html", {"posts": posts})

#def view_post_upper(request, id):
#	post = Post.objects.get(id=id)

#	return render(request, "post_view.html", {"post": post})
