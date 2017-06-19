from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^movies$', views.movies, name='movies'),
    url(r'^screenings', views.screenings, name='screenings'),
    url(r'^tickets', views.tickets, name='tickets'),
]