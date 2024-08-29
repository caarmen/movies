from django.shortcuts import render
from movies.models import Movie


def nplus1(request):
    movies = Movie.objects.all()
    context = {
        "movie_list": movies,
    }

    return render(
        request,
        "movies/full.html",
        context,
    )


def optim(request):
    movies = (
        Movie.objects.select_related("studio", "finance")
        .prefetch_related("actor_set")
        .all()
    )
    context = {
        "movie_list": movies,
    }

    return render(
        request,
        "movies/full.html",
        context,
    )
