from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Video(models.Model):
    movie_id = models.CharField("MovieID", max_length=20, unique=True)
    movie_title = models.CharField("MovieTitle", max_length=200)
    actor1_name = models.CharField("Actor1Name", max_length=100)
    actor2_name = models.CharField("Actor2Name", max_length=100, blank=True)
    director_name = models.CharField("DirectorName", max_length=100)

    GENRE_CHOICES = [
        ('COMEDY', 'Comedy'),
        ('ROMANCE', 'Romance'),
        ('ACTION',  'Action'),
        ('DRAMA',   'Drama'),
        ('SCIFI',   'Sci-Fi'),
        ('HORROR',  'Horror'),
        ('OTHER',   'Other'),
    ]
    movie_genre = models.CharField("MovieGenre", max_length=10, choices=GENRE_CHOICES)

    release_year = models.PositiveIntegerField(
        "ReleaseYear",
        validators=[MinValueValidator(1888), MaxValueValidator(2100)],
    )

    def __str__(self):
        return f"{self.movie_title} ({self.release_year})"
