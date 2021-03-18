# from django.contrib.postgres.fields import ArrayField
from django.db import models


class Contributor(models.Model):
    contributor = models.CharField(max_length=200)

    def __str__(self):
        return self.contributor


class MusicWorks(models.Model):
    iswc = models.CharField(max_length=50, unique=True, null=True)
    title = models.CharField(max_length=200)
    # contributors = ArrayField(models.CharField(max_length=200),default=list)
    contributors = models.ManyToManyField(Contributor)

    def __str__(self):
        return self.iswc
