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
