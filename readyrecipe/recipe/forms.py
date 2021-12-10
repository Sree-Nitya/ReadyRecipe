from django import forms

from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'recipe', 'preparation_time', 'cook_time', 'category']