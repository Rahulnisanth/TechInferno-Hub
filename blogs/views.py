from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


# Create your views here.
def blogs(request):
    blogs = Blog.objects.all()
    context = {"blogs": blogs}
    return render(request, "blogs.html", context)


@login_required(login_url="login_user")
def singleBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.owner = request.user.profile
            comment.blog = blog
            comment.save()
            messages.success(request, "Your Comment was added Successfully!")
            return redirect("single-blog", pk=blog.id)
    context = {"blog": blog, "form": form}
    return render(request, "single-blog.html", context)


@login_required(login_url="login_user")
def toggle_like(request, pk):
    blog = Blog.objects.get(id=pk)
    user = request.user
    if Like.objects.filter(user=user, blog=blog).exists():
        Like.objects.filter(user=user, blog=blog).delete()
        blog.likes.remove(user)
    else:
        Like.objects.create(user=user, blog=blog)
        blog.likes.add(user)
    return redirect("single-blog", pk=pk)
