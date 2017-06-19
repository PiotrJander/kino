from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    poster_url = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Screening(models.Model):
    movie = models.ForeignKey(Movie)
    datetime = models.DateTimeField()
    room = models.CharField(max_length=100)

    def __str__(self):
        return str(self.movie) + str(self.datetime)


class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    screening = models.ForeignKey(Screening)
    user = models.ForeignKey(User)
    seat = models.CharField(max_length=100)

    def __str__(self):
        return str(self.screening) + str(self.user)



