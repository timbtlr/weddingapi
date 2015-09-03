from django.db import models
from s3direct.fields import S3DirectField


class Photo(models.Model):
    full_url = S3DirectField(dest='imgs')
    caption = models.CharField(max_length=200)

    def __unicode__(self):
        return "{} - {}".format(self.full_url, self.caption)
