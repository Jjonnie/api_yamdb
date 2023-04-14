from django.urls import include, path
from rest_framework import routers
from .views import GenreViewSet


router_v1 = routers.DefaultRouter()

router_v1.register('genres', GenreViewSet, basename='genres')

urlpatterns = [
    path("v1/", include(router_v1.urls)),
]