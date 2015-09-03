from django.db import models

# Create your models here.
class RSVP(models.Model):
    name = models.CharField(max_length=200)
    attending = models.BooleanField(default=False)
    plus_one = models.BooleanField(default=False)
    food_choice = models.CharField(max_length=200)
    drink_choice = models.CharField(max_length=200)

    def __unicode__(self): 
        return self.name