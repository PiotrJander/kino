import random

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *


def movies(request):
    movies = Movie.objects.all()
    return render(request, 'kino/movies.html', {'movies': movies})


def screenings(request):
    movie_id = request.GET.get('movie_id')
    if movie_id:
        movie = Movie.objects.get(id=movie_id)
        screenings = Screening.objects.filter(movie=movie)
    else:
        movie = None
        screenings = Screening.objects.all()
    return render(request, 'kino/screenings.html', {'screenings': screenings, 'movie': movie})


def tickets(request):
    if request.method == 'GET':
        lis = User.objects.get(name='lis')
        tickets = Ticket.objects.filter(user=lis)
        return render(request, 'kino/tickets.html', {'tickets': tickets})
    elif request.method == 'POST':
        screening_id = int(request.POST.get('screening_id'))
        user_id = int(request.POST.get('user_id'))
        how_many = int(request.POST.get('how_many'))
        screening = Screening.objects.get(id=screening_id)
        user = User.objects.get(id=user_id)
        for _ in range(how_many):
            seat = random.randint(1, 100)
            Ticket(screening=screening, user=user, seat=str(seat)).save()
        return HttpResponseRedirect(reverse('tickets'))

