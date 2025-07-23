 
from django.contrib import admin
from django.urls import path, include
from . import views

app_name= 'geminisentimentanalysis'
urlpatterns = [
    #path('geminisentiment/', views.GeminiSentiment.as_view(), name="geminisentiment")
    path('geminizeroshot/', views.ZeroShot.as_view(), name="ZeroShot"),
        path('geminifewshots/', views.FewShots.as_view(), name="FewShots"),
]
