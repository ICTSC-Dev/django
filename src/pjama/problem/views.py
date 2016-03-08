from django.contrib.auth.decorators import login_required
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import json
import django_filters
from rest_framework import viewsets, filters ,generics
from .models import Problem,PartialPoint
from .problemSerializer import ProblemSerializer,PartialPointSerializer
# Create your views here.

class ProblemViewSet(viewsets.ModelViewSet,django_filters.FilterSet):
        queryset = Problem.objects.all()
        serializer_class = ProblemSerializer
        filter_backends = (filters.DjangoFilterBackend,)
        filter_fields = ('is_public')


class PartialPointViewSet(viewsets.ModelViewSet):
        queryset = PartialPoint.objects.all()
        serializer_class = PartialPointSerializer

