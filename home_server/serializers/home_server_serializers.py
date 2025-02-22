from rest_framework import serializers
from home_server.models.user import ClientUser

class ClientUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientUser
        exclude = ["password","created_at","last_updated","is_active"]
