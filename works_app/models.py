from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.


from django.db import models


class Work(models.Model):
    title = models.CharField(max_length=250)
    contributors = ArrayField(
        models.CharField(max_length=200, blank=True),
        size=50
    )
    iswc = models.CharField(max_length=200)