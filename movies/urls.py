from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movies', views.movies, name='movies'),
    path('games', views.games, name='games'),
    path('shows', views.shows, name='shows'),
    path('movie-detail/<int:id>', views.movie_detail, name='movie_detail'),
    path('game-detail/<int:id>', views.game_detail, name='game_detail'),
    path('show-detail/<int:id>', views.show_detail, name='show_detail'),
    path('review/<str:media_type>/<int:media_id>/', views.review, name='review'),
]
