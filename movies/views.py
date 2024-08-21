from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from movies.models import Movie
from genres.models import Genre
from movies.forms import MovieModelForm


class MoviesListView(ListView):
    model = Movie
    template_name = 'movies/movies_list.html'
    context_object_name = 'genres' # objeto que irá para template

    def get_queryset(self):
        queryset = Genre.objects.prefetch_related('movies').all()
        search = self.request.GET.get('search')

        if search:
            queryset = queryset.filter(movies__title__icontains=search).distinct()

        return queryset


class MoviesDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'


@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(permission_required('movies.add_movie', raise_exception=True), name='dispatch')
class NewMovieCreateView(CreateView):
    model = Movie
    form_class = MovieModelForm
    template_name = 'movies/new_movie.html'
    success_url = '/movies/'


@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(permission_required('movies.change_movie', raise_exception=True), name='dispatch')
class MovieUpdateView(UpdateView):
    model = Movie
    form_class = MovieModelForm
    template_name = 'movies/movie_update.html'
    success_url = '/movies/'


@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(permission_required('movies.delete_movie', raise_exception=True), name='dispatch')
class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movies/movie_delete.html'
    success_url = '/movies/'
