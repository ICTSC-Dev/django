from django.db import models
from Account.models import Team
from Problems.models import PartialPoint,Problem

# Create your models here.

class Result(models.Model):
    team                     = models.ForeignKey(Team)
    problem                  = models.ForeignKey(Problem)
    score                    = models.IntegerField(default=0)
    is_public                = models.BooleanField(default=False)
    createDate               = models.DateTimeField(null=True, auto_now_add=True)
    updateDate               = models.DateTimeField(blank=True, null=True, auto_now=True)


class Submit(models.Model):
    team                     = models.ForeignKey(Team)
    problem                  = models.ForeignKey
    is_public                = models.BooleanField(default=False)
    add_pont                 = models.IntegerField(default=0)
    createDate               = models.DateTimeField(null=True, auto_now_add=True)
    updateDate               = models.DateTimeField(blank=True, null=True, auto_now=True)


class PartialResult(models.Model):
    submit                   = models.ForeignKey(Submit)
    partialpoint             = models.ForeignKey(PartialPoint)
    is_public                = models.BooleanField(default=False)
    add_pont                 = models.IntegerField(default=0)
    createDate               = models.DateTimeField(null=True, auto_now_add=True)
    updateDate               = models.DateTimeField(blank=True, null=True, auto_now=True)



