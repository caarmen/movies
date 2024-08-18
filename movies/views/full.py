from django.shortcuts import render

from movies.models import Movie


def full(request):
    movies = Movie.objects.all()
    context = {
        "movie_list": movies,
    }

    return render(request, "movies/full.html", context)
