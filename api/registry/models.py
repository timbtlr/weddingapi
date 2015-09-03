from django.db import models

# Create your models here.
class RegistryItem(models.Model):
    name = models.CharField(max_length=200)
    full_url = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    store = models.CharField(max_length=200)
    bought = models.BooleanField(default=False)

    def __unicode__(self):  
        return self.name