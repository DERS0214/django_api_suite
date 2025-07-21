from django.urls import path
from . import views

urlpatterns = [
   path("index/", views.index, name="index"),
   path('', views.index, name='index'),  # Ruta vacía que llama a la vista index
]