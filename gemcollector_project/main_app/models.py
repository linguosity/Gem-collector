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
    
# choices for type of jewelry
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

    gem = models.ForeignKey(Gem, on_delete=models.CASCADE)

    def __str__(self):
        #to make more readable
        return f"{self.get_type_display()}"
    
    class Meta:
        ordering = ['-price']

    