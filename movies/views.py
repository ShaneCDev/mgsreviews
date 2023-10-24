from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from .models import Movie, Game, Show, Review
from .forms import ReviewForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required 


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
    all_reviews = Review.objects.filter(movie=movie)
    paginator = Paginator(all_reviews, 3)
    page = request.GET.get('page')

    try:
        reviews = paginator.page(page)
    except PageNotAnInteger:
        reviews = paginator.page(1)
    except EmptyPage:
        reviews = paginator.page(paginator.num_pages)

    if request.user.is_anonymous:
        context = {
            'movie': movie,
            'all_reviews': all_reviews,
            'reviews': reviews,
        }
    else:
        already_reviewed = all_reviews.filter(author=request.user)
        if already_reviewed:
            reviewed = True
        else:
            reviewed = False
        context = {
            'movie': movie,
            'all_reviews': all_reviews,
            'reviewed': reviewed,
            'reviews': reviews,
        }
    return render(request, 'movie_detail.html', context)


def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)
    all_reviews = Review.objects.filter(game=game)
    paginator = Paginator(all_reviews, 3)
    page = request.GET.get('page')

    try:
        reviews = paginator.page(page)
    except PageNotAnInteger:
        reviews = paginator.page(1)
    except EmptyPage:
        reviews = paginator.page(paginator.num_pages)

    if request.user.is_anonymous:
        context = {
            'game': game,
            'all_reviews': all_reviews,
            'reviews': reviews,
        }
    else:
        already_reviewed = all_reviews.filter(author=request.user)
        if already_reviewed:
            reviewed = True
        else:
            reviewed = False
        context = {
            'game': game,
            'all_reviews': all_reviews,
            'reviews': reviews,
            'reviewed': reviewed,
        }
    return render(request, 'game_detail.html', context)


def show_detail(request, slug):
    show = get_object_or_404(Show, slug=slug)
    all_reviews = Review.objects.filter(show=show)
    paginator = Paginator(all_reviews, 3)
    page = request.GET.get('page')

    try:
        reviews = paginator.page(page)
    except PageNotAnInteger:
        reviews = paginator.page(1)
    except EmptyPage:
        reviews = paginator.page(paginator.num_pages)

    if request.user.is_anonymous:
        context = {
            'show': show,
            'all_reviews': all_reviews,
            'reviews': reviews,
        }
    else:
        already_reviewed = all_reviews.filter(author=request.user)
        if already_reviewed:
            reviewed = True
        else:
            reviewed = False
        context = {
            'show': show,
            'all_reviews': all_reviews,
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


@login_required
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

    if not request.user.is_superuser or request.user != review.author:
        messages.error(request, 'Sorry you can not do that!')
        return redirect(reverse('home'))

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


@login_required
def delete_review(request, id):
    review = get_object_or_404(Review, id=id)

    if not request.user.is_superuser or request.user != review.author:
        messages.error(request, 'Sorry you can not do that!')
        return redirect(reverse('home'))

    if review.media_type == 'movie':
        slug = review.movie.slug
        rev_url = reverse('movie_detail', kwargs={'slug': slug})
    elif review.media_type == 'game':
        slug = review.game.slug
        rev_url = reverse('game_detail', kwargs={'slug': slug})
    elif review.media_type == 'show':
        slug = review.show.slug
        rev_url = reverse('show_detail', kwargs={'slug': slug})
    print(rev_url)
    review.delete()
    return redirect(rev_url)
