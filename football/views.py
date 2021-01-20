from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PlayerDetailsSerializer
from .models import PlayerDetails

# Create your views here.
class PlayerDetailsViewSet(viewsets.ModelViewSet):
    queryset = PlayerDetails.objects.all().order_by('team_name')
    serializer_class = PlayerDetailsSerializer