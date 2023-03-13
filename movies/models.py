from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=3000)
    poster = models.FileField(upload_to='')
    director = models.CharField(max_length=50)
    cast = models.CharField(max_length=100, null=True)
    writer = models.CharField(max_length=50, null=True)
    genre = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title


class Game(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=3000)
    poster = models.FileField(upload_to='')
    developer = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    cast = models.CharField(max_length=100, null=True)
    writer = models.CharField(max_length=50, null=True)
    genre = models.CharField(max_length=100, null=True)
    synopsis = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.title


class Show(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=3000)
    poster = models.FileField(upload_to='')
    cast = models.CharField(max_length=100, null=True)
    writer = models.CharField(max_length=50, null=True)
    genre = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewer')
    review_date = models.DateTimeField(default=timezone.now)
    scores = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10)
    )
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    stars = models.IntegerField(choices=scores)
    comment = models.TextField(max_length=4000)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True, related_name='reviews')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True, blank=True, related_name='reviews')
    show = models.ForeignKey(Show, on_delete=models.CASCADE, null=True, blank=True, related_name='reviews')

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Review {self.comment} by {self.author}'
