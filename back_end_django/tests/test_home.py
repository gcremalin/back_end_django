from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse


class HomeTestCase(TestCase):
    def setUp(self):
    	self.client =Client()
    def test_home(self):
    	# Test that home context returns correct values
    	response = self.client.get(reverse('back_end_django.views.home.current_datetime'))
    	self.assertContains(response, "It is now")
    	