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
    if request.user.is_anonymous:
        context = {
            'movie': movie,
            'reviews': reviews,
        }
    else:
        already_reviewed = reviews.filter(author=request.user)
        if already_reviewed:
            reviewed = True
        else:
            reviewed = False
        context = {
            'movie': movie,
            'reviews': reviews,
            'reviewed': reviewed,
        }
    return render(request, 'movie_detail.html', context)


def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)
    reviews = Review.objects.filter(game=game)
    if request.user.is_anonymous:
        context = {
            'game': game,
            'reviews': reviews,
        }
    else:
        already_reviewed = reviews.filter(author=request.user)
        if already_reviewed:
            reviewed = True
        else:
            reviewed = False
        context = {
            'game': game,
            'reviews': reviews,
            'reviewed': reviewed,
        }
    return render(request, 'game_detail.html', context)


def show_detail(request, slug):
    show = get_object_or_404(Show, slug=slug)
    reviews = Review.objects.filter(show=show)
    if request.user.is_anonymous:
        context = {
            'show': show,
            'reviews': reviews,
        }
    else:
        already_reviewed = reviews.filter(author=request.user)
        if already_reviewed:
            reviewed = True
        else:
            reviewed = False
        context = {
            'show': show,
            'reviews': reviews,
            'reviewed': reviewed,
        }
    return render(request, 'show_detail.html', context)


def review(request, slug, media_type):
    if media_type == 'movie':
        media = get_object_or_404(Movie, slug=slug)
        rev_url = 'movie_detail'
    elif media_type == 'game':
        media = get_object_or_404(Game, slug=slug)
        rev_url = 'game_detail'
    elif media_type == 'show':
        media = get_object_or_404(Show, slug=slug)
        rev_url = 'show_detail'

    if request.method == 'POST':
        form = ReviewForm(request.POST, initial={'author': request.user})
        if form.is_valid():
            review = form.save(commit=False)
            review.media_type = media_type
            review.media_id = media.pk
            if media_type == 'movie':
                review.movie = media
            elif media_type == 'game':
                review.game = media
            elif media_type == 'show':
                review.show = media
            review.save()
            return HttpResponseRedirect(reverse(rev_url, kwargs={'slug': media.slug}))
    else:
        form = ReviewForm(initial={'author': request.user})

    context = {
        'form': form,
    }
    return render(request, 'review.html', context)


def edit_review(request, media_type, slug, id):
    if media_type == 'movie':
        media = get_object_or_404(Movie, slug=slug)
        rev_url = 'movie_detail'
    elif media_type == 'game':
        media = get_object_or_404(Game, slug=slug)
        rev_url = 'game_detail'
    elif media_type == 'show':
        media = get_object_or_404(Show, slug=slug)
        rev_url = 'show_detail'

    review = get_object_or_404(Review, id=id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(rev_url, kwargs={'slug': media.slug}))
    form = ReviewForm(instance=review)
    context = {
        'form': form
    }
    return render(request, 'edit_review.html', context)
