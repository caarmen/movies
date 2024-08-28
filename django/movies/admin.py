from django.contrib import admin
from movies.models import Actor, Finance, Movie, Studio

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Studio)
admin.site.register(Finance)
