from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import permissions
from home_server.models.user import ClientUserToken
from rest_framework import viewsets


class ClientUserTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            return None
        try:
            token = ClientUserToken.objects.get(key=token.split(' ')[1])
            return (token.user, token)
        except ClientUserToken.DoesNotExist:
            raise AuthenticationFailed('Invalid token')


class ClientUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return True
        return False
    

class BaseAuth(viewsets.ViewSet):
    authentication_classes = [ClientUserTokenAuthentication]
    permission_classes = [ClientUserPermission]
    def get_home_server_user(self, request):
        return request.user