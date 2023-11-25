from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Project, Tag
from django.db.models import Q


def paginateProjects(request, projects, results):
    page = request.GET.get("page")
    paginator = Paginator(projects, results)
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)

    leftIndex = int(page) - 4
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = int(page) + 5
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages
    custom_range = range(leftIndex, rightIndex)
    return (custom_range, projects)


def SearchProjects(request):
    search_query = ""
    projects = []
    tags = []
    projects = Project.objects.all()
    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query").split()
        for word in search_query:
            tags.extend(Tag.objects.filter(name__icontains=word))
            projects = Project.objects.distinct().filter(
                Q(title__icontains=word)
                | Q(domain__icontains=word)
                | Q(description__icontains=word)
                | Q(owner__username__icontains=word)
                | Q(tags__in=[tag for tag in tags])
            )
    return projects, search_query
