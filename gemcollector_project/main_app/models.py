from django.db import models
from django.urls import reverse

# Create your models here.

# choices for type of jewelry


class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})

class Gem(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=250)
    weight = models.IntegerField(default=0)
    geotag_location = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    # error resolved with ChatGPT to reference 'gems' model using forward declaration

    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'gem_id': self.id})
  
JEWELRY = (
    ('W', 'Watch'),
    ('E', 'Earrings'),
    ('R', 'Ring'),
    ('B', 'Bracelet'),
    ('N', 'Necklace')
)

class Jewelry(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    url = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    type = models.CharField(
        max_length=1,
        choices=JEWELRY,
        default=JEWELRY[0][0]
    )

    gem = models.ForeignKey(Gem, on_delete=models.CASCADE, related_name='jewelry')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('jewels_detail', kwargs={'pk': self.id})

    