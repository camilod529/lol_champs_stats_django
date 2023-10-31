from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from champions.models import Champion
from champions.serializers import ChampionSerializer


# Create your views here.
class ChampionViewSet(viewsets.ModelViewSet):
    queryset = Champion.objects.all().order_by("name")
    serializer_class = ChampionSerializer
