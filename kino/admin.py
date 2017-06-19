from django.contrib import admin

from .models import Movie, Screening, User, Ticket

admin.site.register(Movie)
admin.site.register(Screening)
admin.site.register(User)
admin.site.register(Ticket)
