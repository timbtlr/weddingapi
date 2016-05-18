from django.db import models

class Invitation(models.Model):
    invite_name = models.CharField(max_length=20, null=True)
    message = models.CharField(max_length=1000, null=True, blank=True)

    def __unicode__(self):
        return self.invite_name

class Invitee(models.Model):
    invitation = models.ForeignKey(Invitation, related_name='invitees')
    name = models.CharField(max_length=200)
    attending = models.NullBooleanField(default=None, null=True, blank=True)

    def __unicode__(self):
        return self.name