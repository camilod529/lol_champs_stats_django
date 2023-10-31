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
        if name := self.kwargs.get("name"):
            champ = Champion.objects.filter(name__contains=name)
            return champ
        if classes := self.kwargs.get("classes"):
            champ = Champion.objects.filter(classes__contains=classes)
            return champ
        if be_price := self.kwargs.get("be_price"):
            champ = Champion.objects.filter(blue_essence_price__gte=be_price).order_by(
                "blue_essence_price"
            )
            return champ
        if rp_price := self.kwargs.get("rp_price"):
            champ = Champion.objects.filter(riot_points_price__gte=rp_price).order_by(
                "riot_points_price"
            )
            return champ
        return super().get_queryset()
