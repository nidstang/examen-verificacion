from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.

class PostManager(models.Manager):
	def create_post(self, title, content):
		post = self.create(title=title, content=content, clikcs=0)
		if isinstance(post, Post):
			return True
		return False

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.CharField(max_length=250)
	clikcs = models.IntegerField()

	objects = PostManager()

class PostForm(ModelForm):
	content = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 20}))
	class Meta:
		model = Post
		fileds = ['title', 'content']
		exclude = ('clikcs')

