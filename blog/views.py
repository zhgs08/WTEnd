from django.shortcuts import render, redirect
from blog.models import Blog
from django.http import HttpResponse, JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt

def index(request):
	return render(request, 'index.html')

def blog_list(request):
	if(request.method == "GET"):
		blogs = Blog.objects.all()
	return render(request, 'blog_list.html', {"blog_list": blogs, "active_menu": "blog"})

def blog_create(request):
	if(request.method == 'POST'):
		title = request.POST['title']
		body = request.POST['body']
		blog = Blog(title=title, body=body)
		blog.save()
		return redirect('blogs')
	return render(request, 'blog_create.html', {"active_menu": "blog"})

def blog_update(request, blog_id):
	try:
		curBlog = Blog.objects.get(pk=blog_id)
	except Exception as e:
		return JsonResponse({"error": str(e)}, status=404)
	if(request.method == "POST"):
		curBlog.title = request.POST['title']
		curBlog.body = request.POST['body']
		curBlog.save()
		return redirect('/blogs')
	return render(request, 'blog_update.html', {"blog": curBlog, "active_menu": "blog"})

@csrf_exempt
def blog_delete(request, blog_id):
	try:
		curBlog = Blog.objects.get(pk=blog_id)
	except Exception as e:
		return JsonResponse({"error": str(e)}, status=404)
	if(request.method == "POST"):
		curBlog.delete()
		return redirect('/blogs')
	return render(request, 'blog_delete.html', {"blog": curBlog, "active_menu": "blog"})
