from rest_framework import serializers
from .models import PlayerDetails

class PlayerDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayerDetails
        fields = ('country', 'league_name', 'team_name', 'player_name', 'player_age', 'position')