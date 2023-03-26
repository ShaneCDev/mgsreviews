from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movies', views.movies, name='movies'),
    path('games', views.games, name='games'),
    path('shows', views.shows, name='shows'),
    path('movie-detail/<slug:slug>', views.movie_detail, name='movie_detail'),
    path('game-detail/<slug:slug>', views.game_detail, name='game_detail'),
    path('show-detail/<slug:slug>', views.show_detail, name='show_detail'),
    path('review/<str:media_type>/<slug:slug>', views.review, name='review'),
]
