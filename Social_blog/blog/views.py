from django.shortcuts import render, redirect
from .models import Blog_post
from .forms import BlogForm

# Create your views here.

def blog_list(request):
    blog = Blog_post.objects.all()
    return render(request, 'blog_list.html',{'blogs':blog})

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog_form.html',{'form':form})