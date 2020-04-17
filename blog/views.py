from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Blog

# Create your views here.
def index(request):
    # all blogs logic here
    blogs = get_list_or_404(Blog)
    return render(request, 'blog/index.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    # blog detail here
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})

def admin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('blog:admin_dashboard'),)
        else:
            return render(request, 'blog/admin_login.html', {'error': 'Invalid credentials'})
    return render(request, 'blog/admin_login.html')

@login_required
def dashboard(request):
    blogs = get_list_or_404(Blog)
    return render(request, 'blog/dashboard.html', {'blogs': blogs})

@login_required
def admin_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:index'))

@login_required
def add_blog(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        blog = Blog.objects.create(title=title, content=content)
        return HttpResponseRedirect(reverse('blog:admin_dashboard'),)
    return render(request, 'blog/add.html')

@login_required
def update_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.content = request.POST['content']
        blog.save()
        return HttpResponseRedirect(reverse('blog:admin_dashboard'),)
    return render(request, 'blog/update.html', {'blog': blog})

@login_required
def view_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/view_blog.html', {'blog':blog})

@login_required
def delete_blog(request, blog_id):
    # delete blog here
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return HttpResponseRedirect(reverse('blog:admin_dashboard'),) 