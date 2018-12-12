from django.urls import path
from . import views

app_name = 'hangman'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new_game, name="new_game"),
    path('guess/', views.guess, name="guess"),
]
