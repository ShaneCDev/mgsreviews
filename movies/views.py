from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
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


def shows(request):
    shows = Show.objects.all()
    context = {
        'shows': shows
    }
    return render(request, 'shows.html', context)


def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
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


def review(request, media_type, media_id):
    if media_type == 'movie':
        media = Movie.objects.get(id=media_id)
    elif media_type == 'game':
        media = Game.objects.get(id=media_id)
    elif media_type == 'show':
        media = Show.objects.get(id=media_id)
    else:
        raise Http404

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.media_type = media_type
            review.media_id = media_id
            if review.media_type == 'movie':
                review.movie = media
            elif review.media_type == 'game':
                review.game = media
            elif review.media_type == 'show':
                review.show = media
            review.save()
    else:
        form = ReviewForm()

    context = {
        'form': form
    }
    return render(request, 'review.html', context)
