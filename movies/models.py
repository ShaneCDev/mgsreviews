from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class MGS(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=3000)
    poster = models.FileField(upload_to='')

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
    stars = models.IntegerField(choices=scores)
    comment = models.TextField(max_length=4000)
    movie = models.ForeignKey(MGS, on_delete=models.CASCADE)

    def __str__(self):
        return self.MGS.title
