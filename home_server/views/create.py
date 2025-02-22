from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
# from homeserver.models.home_server import ClientUser,ClientUserToken
# from homeserver.serializers.home_server_serializers import ClientUserSerializer
from django.contrib.auth.hashers import make_password,check_password
# from homeserver.views.base_auth_token import BaseAuth
from django.views import View
from django.contrib import messages
from django.shortcuts import render,redirect

# views.py
class Signup(View):...
    # def post(self,request):
    #     if request.method == 'POST':
    #         # Retrieve form data
    #         username = request.POST.get('username').strip()
    #         full_name = request.POST.get('full_name').strip() if request.POST.get('full_name') else ""
    #         company_name = request.POST.get('company_name').strip()
    #         email = request.POST.get('email').strip()
    #         phone = request.POST.get('phone').strip()
    #         password = request.POST.get('password')

    #         # Check for duplicate username
    #         if ClientUser.objects.filter(username=username).exists():
    #             messages.error(request, "Username already exists.")
    #             return redirect(request, 'signup')

    #         # Check for duplicate email
    #         if ClientUser.objects.filter(email=email).exists():
    #             messages.error(request, "Email already exists.")
    #             return redirect(request, 'signup')

    #         # Check for duplicate phone
    #         if ClientUser.objects.filter(phone=phone).exists():
    #             messages.error(request, "Phone number already exists.")
    #             return redirect(request, 'signup')

    #         # Check for duplicate company name
    #         if ClientUser.objects.filter(company_name=company_name).exists():
    #             messages.error(request, "Company name already exists.")
    #             return redirect(request, 'signup')

    #         # Create the new user
    #         user = ClientUser(
    #             username=username,
    #             full_name=full_name,
    #             company_name=company_name,
    #             email=email,
    #             phone=phone,
    #         )
    #         # Set the password using Django's set_password to hash it
    #         user.set_password(password)
    #         user.save()

    #         messages.success(request, "Your account has been created successfully! Please log in.")
    #         return redirect(request, 'index')

    #     # If GET request, just render the signup form
    #     return redirect(request, 'signup')



# class LoginClientUserViewset(BaseAuth):
#     def create(self, request):
#         """Authenticate user and return JWT token"""
#         data = request.data
#         identifier = data.get('identifier')  # Email, Phone, or Company Name
#         password = data.get('password')

#         # Check if user exists with email, phone, or company name
#         user = ClientUser.objects.filter(
#             email=identifier.upper()
#         ).first() or ClientUser.objects.filter(
#             phone_number=identifier
#         ).first()

#         if not user:
#             return Response({"error": "User not found!"}, status=status.HTTP_404_NOT_FOUND)

#         # Validate Password
#         if not check_password(password, user.password):
#             return Response({"error": "Invalid password!"}, status=status.HTTP_400_BAD_REQUEST)

#         # Generate or update token
#         if ClientUserToken.objects.filter(user=user).exists():
#             ClientUserToken.objects.get(user=user).delete()
#         token = ClientUserToken.objects.create(user=user)

#         return Response({
#             'user': ClientUserSerializer(user, many=False).data,
#             'Token': token.key
#         }, status=status.HTTP_200_OK)
        