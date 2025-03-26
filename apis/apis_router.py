# apis/apis_router.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PasskeyViewSet
from technical.views.app_control import AppControlAuth

#  Create and register the router for your PasskeyViewSet
router = DefaultRouter()
router.register(r'connect_passkeys', PasskeyViewSet, basename='passkey')
router.register(r'app_access',AppControlAuth, basename='app_access')

urlpatterns = [
    path('', include(router.urls)),  # Include the router
]
