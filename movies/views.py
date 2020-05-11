from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie

class movie_views(ListView):
    model = Movie
    queryset = model.objects.filter(draft=False)
    # def get(self, request):
    #     movies = Movie.objects.all()
    #     return render(request, "movies/movies.html", {"movie_list": movies})

class movie_detail_views(DetailView):
    model = Movie
    slug_field = 'url'
    # def get(self, request, slug):
    #     movie = Movie.objects.get(url = slug)
    #     return render(request, 'movies/movie_detail.html', {"movie": movie})