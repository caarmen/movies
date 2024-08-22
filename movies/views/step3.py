from django.shortcuts import render

from movies.models import Movie


def step3(request):
    # movies = Movie.objects.all()
    movies = Movie.objects.prefetch_related("actor_set").all()
    context = {
        "movie_list": movies,
    }

    return render(request, "movies/step3.html", context)
