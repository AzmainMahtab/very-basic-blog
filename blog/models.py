from django.db import models
from django.utils.timezone import now

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=100, blank=True)
	article = models.TextField(max_length=1000)
	author = models.CharField(max_length=50)
	date = models.DateTimeField(default=now, null=True)

	def __str__(self):
		return self.title