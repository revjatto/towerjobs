from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=150)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	location = models.CharField(max_length=100)
	salary = models.CharField(max_length=20)
	duration = models.CharField(max_length=15)
	date_posted = models.DateTimeField(default=timezone.now)
	contact = models.CharField(max_length=100)
	reference = models.CharField(max_length=25)
	description = models.TextField()
	
	def __str__(self):
		return self.title
        

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})
        


