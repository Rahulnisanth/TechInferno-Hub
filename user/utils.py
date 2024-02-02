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


# def SearchProfiles(request):
#     search_query = ""
#     profiles = Profile.objects.all()
#     skills = []

#     if request.GET.get("search_query"):
#         search_query = request.GET.get("search_query")
#         search_words = search_query.split()
#         filters = []
#         for word in search_words:
#             skills = []
#             skills.extend(Skill.objects.filter(name__icontains=word))
#             try:
#                 year  = int(word)
#                 filters.append(
#                     Q(username__icontains=word)
#                     | Q(job_role__icontains=word)
#                     | Q(location__icontains=word)
#                     | Q(academic_year=year)
#                     | Q(skill__in=[skill for skill in skills])
#                 )
#             except ValueError:
#                 filters.append(
#                     Q(username__icontains=word)
#                     | Q(job_role__icontains=word)
#                     | Q(location__icontains=word)
#                     | Q(skill__in=[skill for skill in skills])
#                 )
#         profiles = Profile.objects.distinct().filter(*filters)
#     else:
#         search_words = []

#     search_query = " ".join(search_words)

#     return profiles, search_query

from django.db.models import Q

# Assuming Profile and Skill are Django models

def SearchProfiles(request):
    search_query = request.GET.get("search_query", "")
    search_words = search_query.split()
    
    filters = []

    for word in search_words:
        try:
            year = int(word)
            filters.append(Q(academic_year=year))
        except ValueError:
            skills = Skill.objects.filter(name__icontains=word)
            filters.append(
                Q(username__icontains=word)
                | Q(job_role__icontains=word)
                | Q(location__icontains=word)
                | Q(skill__in=skills)
            )

    if filters:
        profiles = Profile.objects.filter(*filters).distinct()
    else:
        profiles = Profile.objects.all()

    return profiles, search_query
