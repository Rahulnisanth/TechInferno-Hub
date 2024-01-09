from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import *
from django.db.models import Q


def paginateProfiles(request, profiles, results):
    page = request.GET.get("page")
    paginator = Paginator(profiles, results)
    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    leftIndex = int(page) - 4
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = int(page) + 5
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages
    custom_range = range(leftIndex, rightIndex)
    return (custom_range, profiles)


def SearchProfiles(request):
    search_query = ""
    profiles = []
    skills = []
    profiles = Profile.objects.all()
    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")
        search_words = search_query.split()
        for word in search_words:
            skills = []
            skills.extend(Skill.objects.filter(name__icontains=word))
            profiles = Profile.objects.distinct().filter(
                Q(username__icontains=word)
                | Q(job_role__icontains=word)
                | Q(skill__in=[skill for skill in skills])
            )
    else:
        search_words = []

    search_query = " ".join(search_words)

    return profiles, search_query
