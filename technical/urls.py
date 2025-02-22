from django.urls import path
from .views import read

app_name="operator"
urlpatterns = [
    # Client URLS...For Operator Purpose.........................................................
    path('client_list',read.ClientList.as_view(),name="client_list_urls"),
    path('client_overview',read.ClientOverView.as_view(),name="client_overview_urls"),
    path('update-max-users', read.UpdateMaxUsers.as_view(), name="update_user_limit"),
    path("manage_account", read.ManageAccountID.as_view(), name="manage_account"),
    path("request_check", read.RequestLogView.as_view(), name="req_check_urls"),

]