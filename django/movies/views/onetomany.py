from django.shortcuts import render
from movies.models import Studio


def nplus1(request):
    studios = Studio.objects.all()
    context = {
        "studio_list": studios,
    }

    return render(request, "movies/onetomany.html", context)


def optim(request):
    studios = Studio.objects.all().prefetch_related("movie_set")
    context = {
        "studio_list": studios,
    }

    return render(request, "movies/onetomany.html", context)
