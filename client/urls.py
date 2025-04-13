from django.urls import path
from .views import read

app_name="client"
urlpatterns = [
    # Client URLS...For Operator Purpose.........................................................
    path('client',read.ClientOverView.as_view(),name="client_side_overview_urls"),
    path('request-log', read.RequestLogView.as_view(), name="request_log_urls"),
    path("client_accounts", read.ClientAccountID.as_view(), name="manage_account_client_urls"),
    path('generate-account', read.GeneratePassKey.as_view(), name='generate_account_urls'),

]