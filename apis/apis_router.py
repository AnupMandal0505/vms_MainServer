# apis/apis_router.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PasskeyViewSet

#  Create and register the router for your PasskeyViewSet
router = DefaultRouter()
router.register(r'connect_passkeys', PasskeyViewSet, basename='passkey')

urlpatterns = [
    path('', include(router.urls)),  # Include the router
]
