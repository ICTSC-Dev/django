from django.db import models

# Create your models here.


class Problem(models.Model):
    number                      = models.IntegerField(default=0)
    is_public                   = models.BooleanField(default=False)
    name                        = models.CharField(max_length=255)
    description                 = models.TextField()
    max_point                   = models.IntegerField(default=0)
    created_at                  = models.DateTimeField(null=True, auto_now_add=True)
    updated_at                  = models.DateTimeField(blank=True, null=True, auto_now=True)
    fix_num                     = models.IntegerField(default=0)

    class Meta:
        verbose_name="問題"
        verbose_name_plural="問題一覧"
        ordering=['number']

class PartialPoint(models.Model):
    problem                     = models.ForeignKey(Problem)
    score                       = models.IntegerField(default=0)
    created_at                  =  models.DateTimeField(null=True, auto_now_add=True)
    updated_at                  =  models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        verbose_name="配点情報"
        verbose_name_plural="配点一覧"
        ordering=['created_at']


