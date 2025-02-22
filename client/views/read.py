from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import Group
from home_server.models.user import ClientUser,ClientUserToken
from home_server.models.account import ManageAccount,RequestLog

   
class ClientOverView(View):
    template = "client/dashboard/client_overview.html"
    def get(self, request):
        user=request.user

         # Get all ManageAccount objects related to the client_user
        total_acc_used = ManageAccount.objects.filter(client_user=user,delete_account=False).only("id").count()

        limits = user.limits  # Max users allowed

        # Calculate percentage (avoid division by zero)
        usage_percentage = (total_acc_used / limits) * 100 if limits > 0 else 0  
        context = {
                "client_user": user,
                "total_acc_used": total_acc_used,
                # "acc_users": acc_users,
                "usage_percentage": round(usage_percentage, 2),
            }

        return render(request, self.template,context)
    
    def post(self,request):
        first_name = request.POST.get("first_name").upper()
        last_name = request.POST.get("last_name").upper()
        phone = request.POST.get("phone")
        address = request.POST.get("address").upper()

        # Validate phone number (ensure it's exactly 10 digits)
        if not phone.isdigit() or len(phone) != 10:
            messages.error(request, "Phone number must be exactly 10 digits.")
            return redirect("client:client_side_overview_urls")  # Redirect back to the form page

        # Get the user object
        user = get_object_or_404(ClientUser, username=request.user)
        # Update user details
        user.first_name = first_name
        user.last_name = last_name
        user.phone = str(phone)
        user.address = address
        user.save()

        messages.success(request, "User details updated successfully!")

        return redirect("client:client_side_overview_urls")

class ClientAccountID(View):
    template = "client/dashboard/client_list.html"
    def get(self, request):
        acc_users=ManageAccount.objects.filter(client_user=request.user,delete_account=False)
        context = {
                "acc_users": acc_users,
            }
        return render(request, self.template,context)        
    


class GeneratePassKey(View):
    def get(self, request):
        account_limit = request.user.limits  # Maximum allowed accounts
        use_account = ManageAccount.objects.filter(client_user=request.user,delete_account=False).only("id").count()  # Count existing accounts

        if int(use_account) < int(account_limit):  # Check if under limit
            ManageAccount.objects.create(client_user=request.user)  
            messages.success(request, "Pass Key generated successfully")
        else:
            messages.error(request, f"Your limit is {account_limit}, Please upgrade your plan.")

        return redirect("client:manage_account_client_urls")



class RequestLogView(View):
    template="client/dashboard/request_log.html"
    def get(self,request):
        req=RequestLog.objects.filter(client_user=request.user)
        return render(request,self.template,{"req":req})
    

    def post(self,request):
        if request.method == "POST":
            limits = request.POST.get("limits")
            request_type = request.POST.get("request_type")
            note = request.POST.get("note")

            # Validate user ID and limits
            if  limits:
                messages.error(request, "Invalid input data.")
                return redirect(f"client:client_side_overview_urls")
            
            RequestLog.objects.create(client_user=request.user,note=note,request_type=request_type)


            messages.success(request, "Request message successfully!")
        return redirect(f"client:client_side_overview_urls")

            