from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Game, Show, Review
from .forms import ReviewForm


def home(request):
    movies = Movie.objects.all()
    games = Game.objects.all()
    shows = Show.objects.all()
    context = {
        'movies': movies,
        'games': games,
        'shows': shows
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


def movie_detail(request, id):
    movie = Movie.objects.get(id=id)
    context = {
        'movie': movie
    }
    return render(request, 'movie_detail.html', context)
