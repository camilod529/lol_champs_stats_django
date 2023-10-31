from django.urls import include, path
from rest_framework import routers
from champions import views

router = routers.DefaultRouter()
router.register(r"champions", views.ChampionViewSet)
router.register(r"champions/<int:pk>", views.ChampionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
