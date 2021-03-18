from django.contrib.postgres.fields import ArrayField
from django.db import models

class MusicWorks(models.Model):
    iswc = models.CharField(max_length=50, unique=True, null=True)
    title = models.CharField(max_length=200)
    contributors = ArrayField(models.CharField(max_length=200),default=list)

    def __str__(self):
        return self.iswc
