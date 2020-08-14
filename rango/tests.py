from django.test import TestCase
from rango.models import Category

class CategoryMethodTest(TestCase):
	def test_views_are_positive(self):
		cat = Category(name='test', views=0, likes=0)
		cat.save()
		self.assertEqual((cat.views >= 0), True)
