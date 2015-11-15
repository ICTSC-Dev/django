from django.db import models
from pjama.account.models import Team
from pjama.problem.models import PartialPoint,Problem

# Create your models here.

class Result(models.Model):
    team                     = models.ForeignKey(Team)
    problem                  = models.ForeignKey(Problem)
    score                    = models.IntegerField(default=0)
    is_public                = models.BooleanField(default=False)
    created_at               = models.DateTimeField(null=True, auto_now_add=True)
    updated_at               = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        verbose_name="採点記録"
        verbose_name_plural="採点一覧"
        ordering=['-updated_at']


class Submit(models.Model):
    team                     = models.ForeignKey(Team)
    problem                  = models.ForeignKey(Problem)
    is_public                = models.BooleanField(default=False)
    add_pont                 = models.IntegerField(default=0)
    created_at               = models.DateTimeField(null=True, auto_now_add=True)
    updated_at               = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        verbose_name="提出記録"
        verbose_name_plural="提出記録一覧"
        ordering=['-updated_at']

class PartialResult(models.Model):
    submit                   = models.ForeignKey(Submit)
    partialpoint             = models.ForeignKey(PartialPoint)
    is_public                = models.BooleanField(default=False)
    add_pont                 = models.IntegerField(default=0)
    created_at               = models.DateTimeField(null=True, auto_now_add=True)
    updated_at               = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        verbose_name="配点結果"
        verbose_name_plural="配点結果一覧"
        ordering=['-updated_at']

