from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(default='', max_length=20)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    recipe = models.TextField()
    date = models.DateTimeField(default = timezone.now) #last updated datetime
    preparation_time = models.CharField(default='', max_length=2)
    cook_time = models.CharField(default='', max_length=2)
    category = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return '<ID: {}, Name: {}>'.format(self.id, self.name)
