from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .forms import review_form
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

class add_rewiew(View):
    def post(self, request, pk):
        form = review_form(request.POST)
        movie = Movie.objects.get(id = pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())

