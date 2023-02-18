from django.contrib import admin
from . models import Movie, Review, Game, Show

admin.site.register(Movie)
admin.site.register(Show)
admin.site.register(Game)
admin.site.register(Review)
