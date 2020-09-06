from django.shortcuts import render
from .models import Blog

# Create your views here.
def all_blog(request):
	blogs = Blog.objects.all()
	return render(request, 'blog/all_blog.html', {'blogs': blogs})