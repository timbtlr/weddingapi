from django.db import models

# Create your models here.
class RegistryItem(models.Model):
    store_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    registry_url = models.CharField(max_length=200)
    thumbnail_url = models.URLField(max_length=200)

    def __unicode__(self):  
        return self.store_name