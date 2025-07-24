from django.urls import path
from . import views

app_name = 'ollamasentimentanalysis'

urlpatterns = [
    path('ollamazeroshot/', views.ZeroShot.as_view(), name="ZeroShot"),
    path('ollamafewshots/', views.FewShots.as_view(), name="FewShots"),
    path('ollamachainot/', views.ChainOfThought.as_view(), name="ChainOfThought"),
]
