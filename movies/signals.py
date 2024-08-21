from django.db.models.signals import post_save
from django.dispatch import receiver
from movies.models import Movie, MovieStatistics


def movie_catalog_update():
    movie_count = Movie.objects.all().count() # Contagem de registros
    MovieStatistics.objects.create(
        total_movies=movie_count,
    )

# Para cada filme salvo, será contado quantos filmes há no catálogo
@receiver(post_save, sender=Movie)
def movie_post_save(sender, instance, **kwargs):
    movie_catalog_update()
