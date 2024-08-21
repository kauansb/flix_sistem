from django.db import models
from genres.models import Genre
from actors.models import Actor


class MovieStatistics(models.Model):
    total_movies = models.PositiveIntegerField(default=0)


class Movie(models.Model):
    MATURITY_RATES = [
        ('L', 'Livre'),
        ('10', '10 anos'),
        ('12', '12 anos'),
        ('14', '14 anos'),
        ('16', '16 anos'),
        ('18', '18 anos'),
    ]
    title = models.CharField(max_length=300)
    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        related_name='movies'
    )
    release_date = models.DateField(null=True, blank=True)
    actors = models.ManyToManyField(Actor, related_name='movies')
    resume = models.TextField(null=True, blank=True)
    maturity_rate = models.CharField(
        max_length=2,
        choices=MATURITY_RATES,
        null=True,
        blank=True
        )
    photo = models.ImageField(upload_to='movies/', blank=True, null=True)
    duration = models.DurationField(null=True, blank=True)

    # Retorna a duração formatada como horas e minutos
    def get_duration_display(self):
        total_seconds = int(self.duration.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        return f"{hours}h {minutes}min"

    def __str__(self):
        return self.title
