from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from ClientUser.views.create import LoginClientUserViewset
from home_server.views import read
# from ClientUser.clinet_views import read

# router = DefaultRouter()
# router.register('ClientUsers', ClientUserViewSet, basename='ClientUser')
# router.register('login', LoginClientUserViewset, basename='login')
# router.register('app_access', AppControlAuth, basename='app_access')

app_name="home_urls"
urlpatterns = [
    path('',read.index,name="index_urls"),
    path('auth',read.Auth.as_view(),name="signup_urls"),
    path('signup',read.Auth.as_view(),name="signup"),
    path('signin',read.Signin.as_view(),name="signin_urls"),
    path('logout',read.Logout.as_view(),name="logout_urls"),
    path('dashboard',read.Dashboard.as_view(),name="dashboard_urls"),










    # Client URLS...For OPerator Purpose.........................................................
# path('client/', include(('ClientUser.urls.client_urls', 'client'), namespace="client"))
]