from django.db import models


class Movies(models.Model):
    """
    Model class represents movies_movies table in database.
    """
    movie_title = models.CharField(max_length=50)
    user_rating = models.IntegerField(max_length=2, blank=True)
    critics_rating = models.IntegerField(max_length=2, blank=True)
    running_time_minutes = models.IntegerField(max_length=5, blank=False)
    release_date = models.DateField()
    movie_description = models.TextField(blank=True)

    def __str__(self):
        return self.movie_title