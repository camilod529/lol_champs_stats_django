from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, generics, permissions
from rest_framework.views import Response
from champions.models import Champion
from champions.serializers import ChampionSerializer


# Create your views here.
class ChampionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ChampionSerializer
    queryset = Champion.objects.all()

    def get_queryset(self):
        name = self.kwargs.get("name")
        if name:
            try:
                champ = Champion.objects.filter(name__iexact=name)
                return champ
            except Champion.DoesNotExist:
                return Response({"detail", f"Campeón con nombre {name}no encontrado"}, status=404)
        return super().get_queryset()
