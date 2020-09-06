from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=100)
	article = models.TextField(max_length=1000)
	author = models.CharField(max_length=50)
