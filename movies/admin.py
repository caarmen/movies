from django.contrib import admin

from movies.models import Actor, Movie, MovieFinance, Studio

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Studio)
admin.site.register(MovieFinance)
