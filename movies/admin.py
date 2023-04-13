from django.contrib import admin
from . models import Movie, Review, Game, Show


class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class ShowAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Movie, MovieAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Review)
admin.site.register(Show, ShowAdmin)
