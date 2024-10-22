from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def all_blog(request):
	blog_count = Blog.objects.count
	blogs = Blog.objects.order_by('-date')[:5]
	return render(request, 'blog/all_blog.html', {'blogs': blogs, 'count': blog_count,})

def detail(request, blog_id):
	blog = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'blog/detail.html', {'blog': blog})	