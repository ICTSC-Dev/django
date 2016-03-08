from rest_framework import serializers
from .models import Problem,PartialPoint

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields=('number',
                'is_public',
                'name',
                'description',
                'max_point',
                'created_at',
                'updated_at',
                'fix_num')


class PartialPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartialPoint
        fields=('problem',
                'score',
                'created_at',
                'updated_at')




