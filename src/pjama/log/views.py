from django.contrib.auth.decorators import login_required
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import json
import django_filters
from rest_framework import viewsets, filters
from .models import Result,Submit,PartialResult
from pjama.log.logSerializer import ResultSerializer,SubmitSerializer,PartialResultSerializer
# Create your views here.

class ResultViewSet(viewsets.ModelViewSet):
        queryset = Result.objects.all()
        serializer_class = ResultSerializer
        filter_fields = ('is_public')

class SubmitViewSet(viewsets.ModelViewSet):
        queryset = Submit.objects.all()
        serializer_class = SubmitSerializer
        filter_fields = ('is_public')

class PartialResultViewSet(viewsets.ModelViewSet):
        queryset = PartialResult.objects.all()
        serializer_class = PartialResultSerializer
        filter_fields = ('is_public')
