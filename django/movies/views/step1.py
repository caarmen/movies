from django.shortcuts import render
from movies.models import Movie


def step1(request):
    # movies = Movie.objects.all()
    movies = Movie.objects.all().select_related("finance")
    context = {
        "movie_list": movies,
    }

    return render(request, "movies/step1.html", context)
