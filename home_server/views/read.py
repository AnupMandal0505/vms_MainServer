from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import Group
# from homeserver.models.home_server import ClientUser,ClientUserToken
from ..models.user import ClientUser,ClientUserToken
from ..models.account import ManageAccount,RequestLog
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.models import Group



def index(request):
    template = "home/index.html"
    return render(request,template)

class Auth(View):
    template = "auth/auth.html"

    def get(self, request):
        return render(request, self.template)
    
    def post(self,request):
        if request.method == 'POST':
            # Retrieve form data
            username = request.POST.get('phone_number').upper()
            first_name = request.POST.get('first_name').upper()
            last_name = request.POST.get('last_name').upper()
            company_name = request.POST.get('company_name').upper()
            address = request.POST.get('address').upper()
            email = request.POST.get('email')
            phone = request.POST.get('phone_number')
            password = request.POST.get('password')

            # Check for duplicate username
            if ClientUser.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
                return redirect('home_urls:signup_urls')

            # Check for duplicate email
            if ClientUser.objects.filter(email=email).exists():
                messages.error(request, "Email already exists.")
                return redirect('home_urls:signup_urls')

            # Check for duplicate phone
            if ClientUser.objects.filter(phone=phone).exists():
                messages.error(request, "Phone number already exists.")
                return redirect('home_urls:signup_urls')

            # Check for duplicate company name
            if ClientUser.objects.filter(company_name=company_name).exists():
                messages.error(request, "Company name already exists.")
                return redirect('home_urls:signup_urls')

            # Create the new user
            user = ClientUser(
                username=username,
                first_name=first_name,
                last_name=last_name,
                company_name=company_name,
                address=address,
                email=email,
                phone=phone,
            )
            # Set the password using Django's set_password to hash it
            user.set_password(password)
            user.save()

           # Add user to the default group (change group name as needed)
            default_group_name = "USER"
            group = Group.objects.get(name=default_group_name)  # Get the group
            user.groups.add(group)

            messages.success(request, "Your account has been created successfully! Please log in.")
            return redirect('home_urls:index_urls')

        # If GET request, just render the signup form
        return redirect('home_urls:signup_urls')


class Signin(View):
    def post(self, request):
        print(request.POST)
        identifier=request.POST['identifier']
        password=request.POST['password']
        
        try:
            users=ClientUser.objects.get(username=identifier)  
            user = authenticate(request, username=identifier, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_urls:dashboard_urls')
            else:
                messages.info(request, 'Check Password !')
                return redirect('home_urls:signup_urls')
        except:
            messages.info(request, 'User Not Found !')
        return redirect('home_urls:signup_urls')
    


class Logout(View):
    def get(self, request):
        logout(request)  # Logs out the user
        return redirect("home_urls:index_urls")  # Redirect to login page

class Dashboard(View):
    template = "dashboard/dashboard_home.html"
    def get(self,request):
        operator = ClientUser.objects.filter(groups__name="OPERATOR").count()
        user = ClientUser.objects.filter(groups__name="USER").count()
        client = ClientUser.objects.filter(groups__name="CLIENT").count()
       
        context = {
            "operator": operator,
            "user": user,
            "client": client
        }
        return render(request,self.template,context)


        

class UserListView(View):
    template = "dashboard/user/user_list.html"
    model_name=ClientUser
    groups="CLIENT"
    def get(self, request):
        data_users=self.model_name.objects.filter(groups__name=self.groups)
        # gm_list = self.model_name.objects.filter(roles__name='gm').distinct()
        return render(request, self.template,{"data_users":data_users})
    
class ClientList(UserListView):...

class PaList(UserListView):
    # template = "dashboard/pa/user_list.html"
    # model_name=CustomUser
    roles="pa"




# class AddUserView(View):
#     template = "dashboard/user/add_user.html"
#     model_name=CustomUser
#     roles="gm"
#     def get(self, request):
#         # data_users=self.model_name.objects.filter(roles__name=self.roles)
#         gm_list = self.model_name.objects.filter(roles__name='gm').distinct()

#         return render(request, self.template,{"gm_list":gm_list,"roles":self.roles})
    
#     def post(self,request):
#         if request.method == "POST":
         
#             if self.model_name.objects.filter(phone=request.POST.get("phone")).exists():
#                 messages.info(request,"Already Exists")
#                 return redirect("main_server:dashboard_urls")
#             # Create the user
#             user = self.model_name.objects.create(phone=request.POST.get("phone"), first_name=request.POST.get("first_name"), last_name=request.POST.get("last_name"), email=request.POST.get("email"),password=make_password(request.POST.get("password")))
           
#             # Assign role
#             role_name = self.roles
#             print(role_name)
#             role = Role.objects.get(name=role_name)
#             user.roles.add(role)

#             # Assign GM if selected
#             if request.POST.get("gm"):
#                 gm_user = self.model_name.objects.get(unique_id=request.POST.get("gm"))
#                 user.gm = gm_user
#                 user.save()

#             if self.roles == "gm":
#                 group = Group.objects.get(name="GM")
#             else:
#                 group = Group.objects.get(name="PA")

#             user.groups.add(group)
#         messages.success(request,"Add User Successfull !")
#         return redirect("main_server:dashboard_urls")


# class GmAddUser(AddUserView):...

# class PaAddUser(AddUserView):
#     # template = "dashboard/pa/user_list.html"
#     # model_name=CustomUser
#     roles="pa"






# class UpdateUser(View):
#     def post(self,request):
#         if request.method == "POST":
#             user_id = request.POST.get("user_id")
#             first_name = request.POST.get("first_name")
#             last_name = request.POST.get("last_name")
#             # role = request.POST.get("role")
        

#             user = get_object_or_404(CustomUser, unique_id=user_id)
#             user.first_name = first_name
#             user.last_name = last_name
           
#             # # Assign role
#             # role_name = request.POST.get("role")
#             # role = Role.objects.get(name=role_name)
#             # # user.roles.set(role)

#             # user.roles.set([role])  # Assuming `roles` is ManyToManyField

#             # Retrieve the selected roles from the form (list of strings like ['gm', 'pa'])
#             selected_roles = request.POST.getlist('role')
#             print("roles",selected_roles)
#             # Convert the list of role codes into a queryset of Role objects
#             role_objects = Role.objects.filter(name__in=selected_roles)

            
#             # Update the user's roles to match the selection
#             user.roles.set(role_objects)

#             if request.POST.get("gm"):
#                 user.gm_id = request.POST.get("gm") if request.POST.get("gm") else None
#             user.save()

#             messages.success(request, "User updated successfully!")
#             return redirect("main_server:dashboard_urls")  # Change this to your user list view

#         messages.error(request, "Invalid request.")
#         return redirect("main_server:dashboard_urls")



# class Passkey(View):
#     def post(self,request):
#         try:
#             print(request.POST.get("unique_id"))
#             user=CustomUser.objects.get(unique_id=request.POST.get("unique_id"))
#             user.pass_key=request.POST.get("pass_key")
#             user.save()
#             messages.success(request,"Pass key Added Succcessful")
#             return redirect("main_server:dashboard_urls")
#         except:
#             messages.info(request,"Pass key Added Failed")
#             return redirect("main_server:dashboard_urls")

        