from rest_framework import serializers
from .models import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (  'id',
                    'team_name',
                    'organization',
                    'email',
                    'problem_num',
                    'username',
                    'language',
                    'is_admin',
                    'is_active',
                    'is_staff',
                    'created_at',
                    'updated_at')
#        read_only_fields = ('username',)
