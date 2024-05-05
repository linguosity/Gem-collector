from django.db import models
from django.urls import reverse

# Create your models here.

class Gem(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=250)
    weight = models.IntegerField(default=0)
    geotag_location = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'gem_id': self.id})

