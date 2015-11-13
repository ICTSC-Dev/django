from django.db import models

# Create your models here.


class Problem(models.Model):
    number                      = models.IntegerField(default=0)
    is_public                   = models.BooleanField(default=False)
    name                        = models.CharField(max_length=255)
    markdown                    = models.FileField()
    max_point                   = models.IntegerField(default=0)
    createDate                  = models.DateTimeField(null=True, auto_now_add=True)
    updateDate                  = models.DateTimeField(blank=True, null=True, auto_now=True)
    fix_num                     = models.IntegerField(default=0)

class PartialPoint(models.Model):
    problem                     = models.ForeignKey(Problem)
    score                       = models.IntegerField(default=0)
    createDate                  =  models.DateTimeField(null=True, auto_now_add=True)
    updateDate                  =  models.DateTimeField(blank=True, null=True, auto_now=True)


