from django.urls import path
from . import views

urlpatterns = [
    path("", views.movie_views.as_view()),
    path("<slug:slug>/", views.movie_detail_views.as_view() , name = 'movie_detail'),
    path("review/<int:pk>/", views.add_rewiew.as_view() , name = 'add_review'),
]
