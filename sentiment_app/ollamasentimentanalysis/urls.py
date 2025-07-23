from django.urls import path
from . import views

app_name = 'ollamasentimentanalysis'

urlpatterns = [
    path('ollamazeroshot/', views.ZeroShot.as_view(), name="ZeroShot"),
]
