from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Recipe
from .forms import RecipeForm


def index(request):
    # return HttpResponse('Hello Nitya !')
    if 'q' in request.GET:
        query = request.GET['q']
    else:
        query =''
    recipes = Recipe.objects.filter(name__icontains=query)
    return render(request, 'recipe/index.html', {'recipes': recipes})

def createRecipe(request): 
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = RecipeForm()

    return render(request, 'recipe/createrecipe.html', {'form': form})