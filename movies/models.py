from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=3000)
    poster = models.FileField(upload_to='')
    director = models.CharField(max_length=50)
    carousel_image = models.FileField(upload_to='', null=True)

    def __str__(self):
        return self.title


class Game(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=3000)
    poster = models.FileField(upload_to='')
    developer = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    carousel_image = models.FileField(upload_to='', null=True)

    def __str__(self):
        return self.title


class Show(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    poster = models.FileField(upload_to='')
    carousel_image = models.FileField(upload_to='', null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movie_reviews')
    review_date = models.DateTimeField(default=timezone.now)
    scores = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    stars = models.IntegerField(choices=scores)
    comment = models.TextField(max_length=4000)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    show = models.ForeignKey(Show, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Review {self.comment} by {self.author}'
