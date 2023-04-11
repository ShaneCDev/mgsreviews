from django.test import TestCase
from .models import Movie, Game, Show


class TestViews(TestCase):

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_movies_page(self):
        response = self.client.get('/movies')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movies.html')

    def test_games_page(self):
        response = self.client.get('/games')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'games.html')

    def test_shows_page(self):
        response = self.client.get('/shows')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shows.html')


class TestModels(TestCase):

    def create_movie(self, title='test', description='this is a test', director='testdirector', cast='testcast', writer='testwriter', genre='testgenre'):
        return Movie.objects.create(title=title, description=description, director=director, cast=cast, writer=writer, genre=genre)

    def create_movie_test(self):
        movie = self.create_movie()
        self.assertTrue(isinstance(movie, Movie))
        self.assertEqual(movie.__str__, movie.title)
