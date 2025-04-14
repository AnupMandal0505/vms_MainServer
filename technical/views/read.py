from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import Group
from home_server.models.user import ClientUser,ClientUserToken,UserLimitHistory
from home_server.models.account import ManageAccount,RequestLog
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse

from django.contrib.auth.models import Group


class ClientList(View):
    template = "dashboard/operator/client_list.html"
    def get(self, request):
        data_users=ClientUser.objects.filter(groups__name="CLIENT")
        return render(request, self.template,{"data_users":data_users})
    

    
    
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
import uuid

>>>>>>> dev_anup
>>>>>>> dev_anup_squashed
class ClientOverView(View):
    template = "dashboard/operator/client_overview.html"
    def get(self, request):
        
<<<<<<< HEAD
        client_user=ClientUser.objects.get(id=request.GET.get("id"))
=======
<<<<<<< HEAD
        client_user=ClientUser.objects.get(id=request.GET.get("id"))
=======
        client_id_str = request.GET.get("id")  # instead of "client_id"

        # client_user=ClientUser.objects.get(id=uuid.UUID(request.GET.get("client_id")))
        try:
            client_id = uuid.UUID(client_id_str)
            client_user = ClientUser.objects.get(id=client_id)
        except (ValueError, TypeError, ClientUser.DoesNotExist):
            messages.error(request, "Invalid or missing client ID.")
            return redirect("some_fallback_url")  # Optional fallback
>>>>>>> dev_anup
>>>>>>> dev_anup_squashed

        # Get all ManageAccount objects related to the client_user
        acc_users = ManageAccount.objects.filter(client_user=request.GET.get("id"))

        # Count only those where delete_account=False
        total_acc_used = acc_users.filter(delete_account=False).count()

        limits = client_user.limits  # Max users allowed
        # Calculate percentage (avoid division by zero)
        usage_percentage = (total_acc_used / limits) * 100 if limits > 0 else 0  
        context = {
                "client_user": client_user,
                "total_acc_used": total_acc_used,
                "acc_users": acc_users,
                "usage_percentage": round(usage_percentage, 2),
            }

        return render(request, self.template,context)
    

    def post(self,request):
        # user_id = request.POST.get("user_id")
        # print(user_id)
        first_name = request.POST.get("first_name").upper()
        last_name = request.POST.get("last_name").upper()
        phone = request.POST.get("phone")
        address = request.POST.get("address").upper()


        redirect_url = f"{reverse('operator:client_overview_urls')}?id={request.GET.get('id')}"  # Correct way to format URL
        # Validate phone number (ensure it's exactly 10 digits)
        if not phone.isdigit() or len(phone) != 10:
            messages.error(request, "Phone number must be exactly 10 digits.")
            return redirect(redirect_url)

        # Get the user object
        user = get_object_or_404(ClientUser, id=request.GET.get("id"))
        print(user)
        # Update user details
        user.first_name = first_name
        user.last_name = last_name
        user.phone = str(phone)
        user.address = address
        user.save()

        messages.success(request, "User details updated successfully!")

        return redirect(redirect_url)



class UpdateMaxUsers(View):
    def post(self,request):
        try:
            user_id=request.POST.get("user_id")
            user = ClientUser.objects.get(id=user_id)
            transaction_type = request.POST.get("transaction_type")  # Get transaction type from request
            new_limit = int(request.POST.get("new_limit"))  # Get limits from request


            redirect_url = f"{reverse('operator:client_overview_urls')}?id={user_id}"  # Correct way to format URL

            # Validate transaction type
            if transaction_type not in ["increase_limit", "decrease_limit"]:
                messages.error(request, "Invalid transaction type.")
                return redirect(redirect_url)

            # Create transaction record
            transaction = UserLimitHistory.objects.create(
                account=user, transaction_type=transaction_type, new_limit =new_limit
            )

            # Update user limits based on transaction type
            if transaction_type == "increase_limit":
                user.limits += new_limit
            elif transaction_type == "decrease_limit":
                if user.limits - new_limit >= 5:  # Ensure limits remains at least 5
                    user.limits -= new_limit
                else:
                    messages.error(request, "limits cannot be less than 5.")
                    return redirect(redirect_url)

            user.save()

            messages.success(request, "Plan updated successfully!")
            return redirect(redirect_url)

        except ValueError:
            messages.error(request, "Invalid number format.")
            return redirect(redirect_url)

        except ClientUser.DoesNotExist:
            messages.error(request, "User not found.")
            return redirect(redirect_url)





#  'user_id': [''], 'status': ['deactivate'], 'delete': ['on']}>
#  'user_id': [''], 'status': ['activate'], 'delete': ['on']}>
class ManageAccountID(View): # Control Client ID activate/deactivate and Client User Id activate/deactivate
    def post(self,request):
        print(request.POST)

        try:
            acc = ManageAccount.objects.get(id=request.POST.get("user_id"))
            if 'on' == request.POST.get("delete"):
                acc.delete_account = True
            else:
                acc.delete_account = False


            if 'deactivate' == request.POST.get("status"):
                acc.is_on_hold = True
            else:
                acc.is_on_hold = False

            
            acc.save()

            messages.success(request, "Plan updated successfully!")
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> dev_anup_squashed
            return redirect(f"operator:client_overview_urls", acc.client_user.id)

        except ValueError:
            messages.error(request, "Invalid number format.")
            return redirect(f"operator:client_overview_urls", acc.client_user.id)
<<<<<<< HEAD
=======
=======
            return redirect(f"{reverse('operator:client_overview_urls')}?id={acc.client_user.id}")
            # return redirect("operator:client_overview_urls")

        except ValueError:
            messages.error(request, "Invalid number format.")
            return redirect(f"{reverse('operator:client_overview_urls')}?id={acc.client_user.id}")
>>>>>>> dev_anup
>>>>>>> dev_anup_squashed


        except ManageAccount.DoesNotExist:
            messages.error(request, "User not found.")
<<<<<<< HEAD
            return redirect(f"operator:client_overview_urls", acc.client_user.id)
=======
<<<<<<< HEAD
            return redirect(f"operator:client_overview_urls", acc.client_user.id)
=======
            return redirect(f"{reverse('operator:client_overview_urls')}?id={acc.client_user.id}")
>>>>>>> dev_anup
>>>>>>> dev_anup_squashed




class RequestLogView(View):
    template="dashboard/operator/request_log.html"
    def get(self,request):
        req=RequestLog.objects.filter(status="pending")
        return render(request,self.template,{"req":req})
    
    def post(self,request):
        try:
            r=RequestLog.objects.get(id=request.POST.get("client_user_id"))
            r.status=request.POST.get("status")
            r.save()
            messages.success(request,"Status Update Successfull")
            return redirect("operator:req_check_urls")
        except Exception as e:
            print(e)
            messages.success(request,"Status not Update")
            return redirect("operator:req_check_urls")