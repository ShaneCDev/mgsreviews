from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Game, Show


def home(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'index.html', context)


def movies(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies.html', context)


def games(request):
    games = Game.objects.all()
    context = {
        'games': games
    }
    return render(request, 'games.html', context)
