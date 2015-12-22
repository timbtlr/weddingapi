from django.db import models

class Invitation(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    message = models.CharField(max_length=1000, null=True, blank=True)

    def __unicode__(self):
        return self.id

class Invitee(models.Model):
    invitation = models.ForeignKey(Invitation, related_name='invitees')
    name = models.CharField(max_length=200)
    attending = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name