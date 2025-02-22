from django.urls import include, path

urlpatterns = [
    path('', include(('home_server.urls.urls', 'home'), namespace="home")),  # ✅ Fix 'home' namespace
    # path('operator/', include(('home_server.urls.operator_urls', 'client'), namespace="operator")),  # ✅ Fix 'client' namespace
]
