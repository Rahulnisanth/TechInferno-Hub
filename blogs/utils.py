from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Blog
from django.db.models import Q


def paginateBlogs(request, blogs, results):
    page = request.GET.get("page")
    paginator = Paginator(blogs, results)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        blogs = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        blogs = paginator.page(page)

    leftIndex = int(page) - 4
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = int(page) + 5
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages
    custom_range = range(leftIndex, rightIndex)
    return (custom_range, blogs)


def SearchBlogs(request):
    search_query = ""
    blogs = []
    blogs = Blog.objects.all()
    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query").split()
        for word in search_query:
            blogs = Blog.objects.distinct().filter(
                Q(title__icontains=word) | Q(owner__username__icontains=word)
            )
    return blogs, search_query
