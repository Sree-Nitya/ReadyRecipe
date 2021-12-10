from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('createRecipe/', views.createRecipe, name='createRecipe'),
]