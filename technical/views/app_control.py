from rest_framework import viewsets, status
from rest_framework.response import Response
from home_server.models.account import ManageAccount



class AppControlAuth(viewsets.ViewSet):
    def create(self,request):
        pass_key = request.data.get("pass_key")
        phone = request.data.get("phone")

        if not pass_key or not phone:
            return Response({"error": "Missing pass_key or phone"}, status=status.HTTP_400_BAD_REQUEST)

        user_exists = ManageAccount.objects.filter(pass_key=pass_key, phone=phone,is_on_hold=False).exists()

        if user_exists:
            return Response({"RES": True}, status=status.HTTP_200_OK)
        else:
            return Response({"ERR": False}, status=status.HTTP_404_NOT_FOUND)