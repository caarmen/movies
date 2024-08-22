from django.shortcuts import render

from movies.models import Movie


def step2(request):
    # movies = Movie.objects.all()
    movies = Movie.objects.all().select_related("studio")
    context = {
        "movie_list": movies,
    }

    return render(request, "movies/step2.html", context)
