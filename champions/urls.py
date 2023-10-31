from django.urls import include, path
from rest_framework import routers
from champions import views

router = routers.DefaultRouter()
router.register(r"champions", views.ChampionViewSet, basename="champions")
router.register(r"champions/<int:pk>", views.ChampionViewSet, basename="champions-by-id")


urlpatterns = [
    path("", include(router.urls)),
    path(
        "champions/name/<str:name>/",
        views.ChampionViewSet.as_view(actions={"get": "list"}),
        name="champion-detail-by-name",
    ),
]
