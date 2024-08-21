from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from movies.views import MoviesListView, MoviesDetailView, NewMovieCreateView, MovieUpdateView, MovieDeleteView
from accounts.views import RegisterView, LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login' ),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('movies/', MoviesListView.as_view(), name='movies_list'),
    path('movies/<int:pk>/', MoviesDetailView.as_view(), name='movie_detail'),
    path('movie/<int:pk>/update/', MovieUpdateView.as_view(), name='movie_update'),
    path('movie/<int:pk>/delete/', MovieDeleteView.as_view(), name='movie_delete'),
    path('new_movie/', NewMovieCreateView.as_view(), name='new_movie'),

]

# Habilita uso de mídias no projeto
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
