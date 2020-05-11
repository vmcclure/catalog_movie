from django.contrib import admin

# Register your models here.
from .models import Category, MovieShots, RatingStar, Reviews, Actor, Genre,Movie,Rating
admin.site.register(Actor)
admin.site.register(Category)
admin.site.register(MovieShots)
admin.site.register(RatingStar)
admin.site.register(Reviews)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Rating)
