from django.db import models

# Create your models here.

class MAC(models.Model):
    nimi = models.CharField(max_length=100)
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=200)


    def __str__(self):
        return self.nimi
    


