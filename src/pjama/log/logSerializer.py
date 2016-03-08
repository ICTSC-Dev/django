from rest_framework import serializers
from pjama.account.accountSerializer import TeamSerializer
from pjama.problem.problemSerializer import ProblemSerializer
from .models import Result,Submit,PartialResult

class ResultSerializer(serializers.ModelSerializer):
    team=TeamSerializer()
    problem=ProblemSerializer()
    class Meta:
        model=Result
        fields=('team',
                'problem',
                'score',
                'is_public',
                'created_at',
                'updated_at')


class SubmitSerializer(serializers.ModelSerializer):
    team=TeamSerializer()
    problem=ProblemSerializer()
    class Meta:
        model=Submit
        fields=('team',
                'problem',
                'is_public',
                'add_pont',
                'created_at',
                'updated_at')


class PartialResultSerializer(serializers.ModelSerializer):
    submit=SubmitSerializer()
    class Meta:
        model=PartialResult
        fields=('submit',
                'partialpoint',
                'is_public',
                'add_pont',
                'created_at',
                'updated_at')
