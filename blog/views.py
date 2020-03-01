from django.shortcuts import render
from .models import Post

def index(request):
	data = Post.objects.all()
	context = {
		'posts':data
	}
	return render(request, 'blog/index.html', context=context)

def about(request):
	return HttpResponse("This is an about page.")
