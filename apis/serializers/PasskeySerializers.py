from rest_framework import serializers
from home_server.models.account import ManageAccount

class PasskeySerializer(serializers.ModelSerializer):
    class Meta:
        model = ManageAccount
        fields = ['phone','pass_key']


# class PasskeySerializer(serializers.ModelSerializer):
#     username = serializers.SerializerMethodField()

#     class Meta:
#         model = ManageAccount
#         fields = ['username', 'phone', 'pass_key', 'otp']

#     def get_username(self, obj):
#         return obj.client_user.username