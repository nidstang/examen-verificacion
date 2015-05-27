"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase, RequestFactory

import unittest
import mock

from blog.models import Post, PostManager
from blog.views import home, create_post
from util import Util


class TestUtil(TestCase):
    def test_upper_string(self):
    	result = Util.string_to_upper("test")
    	self.assertEqual(result, "TEST")

    def test_cut_string(self):
    	result = Util.cut_string("hellothisisateswithstring")
    	self.assertEqual(result, "hellothisisates...")

class TestPostViewRequest(TestCase):
	def setUp(self):
		self.factory = RequestFactory()
	def test_request_home(self):
		request = self.factory.get('/home')

		response = home(request)

		self.assertEqual(response.status_code, 200)

	def test_request_create(self):
		request = self.factory.get('/create')

		response = home(request)

		self.assertEqual(response.status_code, 200)

	def test_request_posts(self):
		request = self.factory.get('/posts')

		response = home(request)

		self.assertEqual(response.status_code, 200)

	@mock.patch('blog.models.PostManager.create', mock.Mock())
	def test_create_post(self):
		title = "This is a test"
		content = "The gate to star"
		clikcs = 0

		# Que el mock devuelva True. Que seria en el caso de insertarse
		PostManager.create.side_effect = [True]

		request = self.factory.post('/create/', data={'title': title, 'content': content})
		request._dont_enforce_csrf_checks = True

		response = create_post(request)

		# Que se haya creado el post
		PostManager.create.assert_called_with(title=title, content=content, clikcs=clikcs)

		self.assertEqual(response.status_code, 200)

	




        
