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
    path(
        "champions/classes/<str:classes>/",
        views.ChampionViewSet.as_view(actions={"get": "list"}),
        name="champion-detail-by-classes",
    ),
    path(
        "champions/price/ea/<int:be_price>/",
        views.ChampionViewSet.as_view(actions={"get": "list"}),
        name="champion-detail-by-be-price",
    ),
    path(
        "champions/price/rp/<int:rp_price>/",
        views.ChampionViewSet.as_view(actions={"get": "list"}),
        name="champion-detail-by-rp-price",
    ),
]
