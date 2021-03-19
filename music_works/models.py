from django.db import models
from model_utils.models import TimeStampedModel


class Contributor(TimeStampedModel):
    contributor = models.CharField(max_length=200)

    def __str__(self):
        return self.contributor


class MusicWorks(TimeStampedModel):
    iswc = models.CharField(max_length=50, unique=True, null=True)
    title = models.CharField(max_length=200)
    contributors = models.ManyToManyField(Contributor)

    def __str__(self):
        return self.iswc
