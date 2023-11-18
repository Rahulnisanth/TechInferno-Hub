from django.shortcuts import render
from .models import *


# Create your views here.
def blogs(request):
    blogs = Blog.objects.all()
    context = {"blogs": blogs}
    return render(request, "blogs.html", context)


def singleBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    context = {"blog": blog}
    return render(request, "single-blog.html", context)
