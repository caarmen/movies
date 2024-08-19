from django.shortcuts import render

from movies.models import Movie


def full(request):
    # movies = Movie.objects.select_related("studio").select_related("finance").prefetch_related("actor_set").all()
    movies = Movie.objects.all()
    context = {
        "movie_list": movies,
    }

    return render(request, "movies/full.html", context)
