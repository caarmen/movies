import csv

from django.core.management.base import BaseCommand
from movies.models import Actor, Finance, Movie, Studio


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Delete all data
        Movie.objects.all().delete()
        Studio.objects.all().delete()
        Actor.objects.all().delete()

        with open("../data/studios.csv") as studios_file, open(
            "../data/actors.csv"
        ) as actors_file, open("../data/movies.csv") as movies_file, open(
            "../data/actor_movies.csv"
        ) as actor_movies_file:
            studios_reader = csv.DictReader(studios_file)
            actors_reader = csv.DictReader(actors_file)
            movies_reader = csv.DictReader(movies_file)
            actor_movies_reader = csv.DictReader(actor_movies_file)

            for studio_line in studios_reader:
                Studio.objects.create(**studio_line)

            for actor_line in actors_reader:
                Actor.objects.create(**actor_line)

            for movie_line in movies_reader:
                movie = Movie.objects.create(
                    title=movie_line["title"],
                    release_year=int(movie_line["release_year"]),
                    studio=Studio.objects.get(name=movie_line["studio"]),
                )

                movie.finance = Finance.objects.create(
                    movie=movie,
                    budget=float(movie_line["budget"]),
                    box_office=float(movie_line["box_office"]),
                )
                movie.save()

            for actor_movie_line in actor_movies_reader:
                actor = Actor.objects.get(
                    first_name=actor_movie_line["first_name"],
                    last_name=actor_movie_line["last_name"],
                )
                movie = Movie.objects.get(
                    title=actor_movie_line["title"],
                )

                actor.movies.add(movie)
