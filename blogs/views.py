from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .utils import *


def blogs(request):
    blogs, search_query = SearchBlogs(request)
    custom_range, blogs = paginateBlogs(request, blogs, 9)
    context = {
        "blogs": blogs,
        "search_query": search_query,
        "custom_range": custom_range,
    }
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
    context = {
        "blog": blog,
        "form": form,
    }
    return render(request, "single-blog.html", context)


@login_required(login_url="login_user")
def createBlog(request):
    profile = request.user.profile
    blog_form = BlogForm(instance=profile)
    if request.method == "POST":
        blog_form = BlogForm(request.POST)
        if blog_form.is_valid():
            blog = blog_form.save(commit=False)
            blog.owner = profile
            blog.save()
            messages.success(request, f"{blog.title} was posted successfully!")
            return redirect("blogs")
    context = {"form": blog_form}
    return render(request, "blog_form.html", context)


@login_required(login_url="login_user")
def editBlog(request, pk):
    profile = request.user.profile
    blog = profile.blog_set.get(id=pk)
    blog_form = BlogForm(instance=blog)
    if request.method == "POST":
        blog_form = BlogForm(request.POST, request.FILES, instance=blog)
        if blog_form.is_valid():
            blog_form.save()
            messages.success(request, "Blog Post was updated Successfully!")
            return redirect("blogs")
    context = {"form": blog_form, "blog": blog}
    return render(request, "blog_form.html", context)


@login_required(login_url="login_user")
def deleteBlog(request, pk):
    profile = request.user.profile
    blog = profile.blog_set.get(id=pk)
    if request.method == "POST":
        blog.delete()
        messages.error(request, "Blog was deleted Successfully!")
        return redirect("blogs")
    context = {"blog": blog}
    return render(request, "delete-blog.html", context)


@login_required(login_url="login_user")
def likeBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    if request.method == "GET":
        user = request.user.profile
        if user not in blog.like.all():
            blog.like.add(user)
        else:
            blog.like.remove(user)
        return redirect("single-blog", pk=pk)
    return render(request, "single-blog.html")
