from django.shortcuts import render
from movies.models import Movie


def nplus1(request):
    movies = Movie.objects.all()
    context = {
        "movie_list": movies,
    }

    return render(request, "movies/manytoone.html", context)


def optim(request):
    movies = Movie.objects.all().select_related("studio")
    context = {
        "movie_list": movies,
    }

    return render(request, "movies/manytoone.html", context)
