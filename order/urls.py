from django.urls import path, inclube
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

router = DefaultRouter()
router.register("ordr", OrderViewSet)

urlpatterns = [
    path(""), isinstance
]