from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import UserLoginViewSet

router = DefaultRouter()
router.register("userlogin", UserLoginViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
