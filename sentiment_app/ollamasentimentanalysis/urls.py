 
from django.contrib import admin
from django.urls import path, include
from . import views

app_name= 'ollamasentimentanalysis'
urlpatterns = [
    path('ollamasentiment/', views.OllamaSentiment.as_view(), name="ollamasentiment")
]
