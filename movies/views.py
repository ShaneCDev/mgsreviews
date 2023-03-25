from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import Http404, HttpResponseRedirect
from .models import Movie, Game, Show, Review
from .forms import ReviewForm
from django.shortcuts import resolve_url


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


def shows(request):
    shows = Show.objects.all()
    context = {
        'shows': shows
    }
    return render(request, 'shows.html', context)


def movie_detail(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    reviews = Review.objects.filter(movie=movie)
    context = {
        'movie': movie,
        'reviews': reviews,
    }
    return render(request, 'movie_detail.html', context)


def game_detail(request, id):
    game = Game.objects.get(id=id)
    context = {
        'game': game,
        'media_type': 'game',
        'media_id': id,
    }
    return render(request, 'game_detail.html', context)


def show_detail(request, id):
    show = Show.objects.get(id=id)
    context = {
        'show': show,
        'media_type': 'show',
        'media_id': id,
    }
    return render(request, 'show_detail.html', context)


def review(request, slug, media_type):
    if media_type == 'movie':
        media = get_object_or_404(Movie, slug=slug)

    if request.method == 'POST':
        form = ReviewForm(request.POST, initial={'author': request.user})
        if form.is_valid():
            review = form.save(commit=False)
            review.media_type = media.media_type
            review.media_id = media.pk

            if media.media_type == 'movie':
                review.movie = media
            review.save()         
    else:
        form = ReviewForm(initial={'author': request.user})

    context = {
        'form': form
    }
    return render(request, 'review.html', context)
