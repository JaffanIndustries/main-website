from __future__ import unicode_literals

from django.db import models

# Create your models here.
class about(models.Model):
	content = models.CharField(max_length=400)
	created = models.DateTimeField(auto_created=True, auto_now=False)
	updated = models.DateTimeField(auto_now=True, auto_created=False)

	def __str__(self):
		return self.content

class services(models.Model):
	name = models.CharField(max_length=20)
	description = models.CharField(max_length=300)
#	image = models.ImageField(image_path='')
	created = models.DateTimeField(auto_created=True, auto_now=False)
	updated = models.DateTimeField(auto_now=True, auto_created=False)

	def __str__(self):
		return self.name

	"""docstring for services"""
	def __init__(self, arg):
		super(services, self).__init__()
		self.arg = arg

class update(models.Model):
	short_description = models.CharField(max_length=40)
	description = models.CharField(max_length=300)
	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_created=True, auto_now=False)
	updated = models.DateTimeField(auto_now=True, auto_created=False)	

	def __str__(self):
		return self.short_description

class product(models.Model):
	name = models.CharField(max_length=30)
	short_description = models.CharField(max_length=40)
	description = models.CharField(max_length=400)
#	image = models.ImageField(image_path='')
	created = models.DateTimeField(auto_created=True, auto_now=False)
	updated = models.DateTimeField(auto_now=True, auto_created=False)		