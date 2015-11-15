from django.contrib import admin
from pjama.log.models import Result,Submit,PartialResult
# Register your models here.

admin.site.register(Result)
admin.site.register(Submit)
admin.site.register(PartialResult)

