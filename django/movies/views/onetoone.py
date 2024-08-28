from django.shortcuts import render
from movies.models import Movie


def nplus1(request):
    movies = Movie.objects.all()
    context = {
        "movie_list": movies,
    }

    return render(
        request,
        "movies/onetoone.html",
        context,
    )


def optim(request):
    movies = Movie.objects.all().select_related("finance")
    context = {
        "movie_list": movies,
    }

    return render(
        request,
        "movies/onetoone.html",
        context,
    )
