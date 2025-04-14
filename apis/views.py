from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from home_server.models.account import ManageAccount
from .serializers.PasskeySerializers import PasskeySerializer
import random
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string
# from django.conf import settings
from apis.tasks import send_verification_email



# def mail(name,email,otp,subject,message,template_name):
#     try:
#         from_email = settings.EMAIL_HOST_USER
        
#         # Correct template_path and render the HTML template with the provided data
#         # template_path = 'mail/otp.html'
#         # Render the HTML template to a string
#         template_path = f'mail/{template_name}.html'
#         context = {
#             'name': name,
#             'otp': otp,
#             'message':message,
#             'email':email,
#         }
        
#         # Render the HTML template to a string
#         message = render_to_string(template_path, context)
        
#         to = "anupmandal828109@gmail.com"
        
#         # Create an email message object and attach the HTML message
#         msg = EmailMultiAlternatives(subject, '', from_email, [to])
#         msg.attach_alternative(message, 'text/html')
#         try:
#             msg.send()
#         except Exception as e:
#             print("Error sending email:", e)
#             raise Exception("Problem sending email check password")
        
#     except Exception as e:
#         print("Error sending email:", e)
#         raise Exception("Problem sending email")




# Function to generate a random 6-digit OTP
def generate_otp():
    """Generate a random 6-digit OTP"""
    return str(random.randint(100000, 999999))

class PasskeyViewSet(viewsets.ViewSet):

    # GET method to verify the passkey and send OTP via email
    def list(self, request):
        serializer = PasskeySerializer(data=request.data)

        passkey = request.GET.get('passkey')
        client_user = request.GET.get('client_user')
        try:
            # Check if the passkey exists in the database
            passkey_obj = ManageAccount.objects.get(pass_key=passkey)  

            # If phone is not None, passkey is already used
            if passkey_obj.phone is not None:
                return Response({"error": "Passkey already used"}, status=status.HTTP_400_BAD_REQUEST)
        
            new_otp=generate_otp()
            passkey_obj.otp=new_otp  # This should be `passkey_obj.otp = generate_otp()`
            passkey_obj.save()

            # Send emails
            # mail(passkey_obj.client_user.first_name, passkey_obj.client_user.email, new_otp, 'OTP Verification', 'Please enter this OTP to complete the verification process.','otp')
            send_verification_email.delay(
                passkey_obj.client_user.first_name,
                passkey_obj.client_user.email,
                new_otp,
                'OTP Verification',
                'Please enter this OTP to complete the verification process.',
                'otp'
            )

            
            return Response({"success": f"Email sent to {passkey_obj.client_user.email}"}, status=status.HTTP_200_OK)

        except ManageAccount.DoesNotExist:
            # If passkey does not exist, return an error response
            return Response({"error": "Invalid Passkey"}, status=status.HTTP_400_BAD_REQUEST)

        # If serializer is not valid, return validation errors
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # POST method to verify OTP and update phone number
    def create(self, request):
        serializer = PasskeySerializer(data=request.data)
        # if serializer.is_valid():
        passkey = request.data.get("passkey")  # ✅ Correct way to get passkey
        otp = request.data.get("otp")
        phone = request.data.get("unique_phone")
        # client_user = request.data.get("client_user")
        print(request.data)
        try:
            # Check if the passkey exists
            passkey_obj = ManageAccount.objects.get(pass_key=passkey)  

            # If phone is already set, passkey has been used before
            if passkey_obj.phone is not None:
                return Response({"error": "Passkey already used"}, status=status.HTTP_400_BAD_REQUEST)

            # Check if the OTP is valid
            if passkey_obj.otp != otp:  # Ensure OTP is stored in `ManageAccount`
                return Response({"error": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)

            # If everything is valid, update the phone and save changes
            passkey_obj.phone = phone
            passkey_obj.save()


            # Send emails
            # mail(passkey_obj.client_user.first_name, passkey_obj.client_user.email, 'new_otp', 'Passkey Connection Successful', 'Congratulations! Your passkey connection has been successfully established.','passkey_success')
            send_verification_email.delay(
                passkey_obj.client_user.first_name,
                passkey_obj.client_user.email,
                'new_otp',
                'Passkey Connection Successful',
                'Passkey Connection Successful', 'Congratulations! Your passkey connection has been successfully established.',
                'passkey_success'
            )

            
            return Response({"success": "Saved successfully"}, status=status.HTTP_200_OK)

        except ManageAccount.DoesNotExist:
            # If the passkey is invalid, return an error response
            return Response({"error": "Invalid Passkey"}, status=status.HTTP_400_BAD_REQUEST)

        # # If serializer validation fails, return errors
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
