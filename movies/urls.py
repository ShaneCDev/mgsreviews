from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movies', views.movies, name='movies'),
    path('games', views.games, name='games'),
    path('movie-detail/<int:id>', views.movie_detail, name='movie_detail')
]
