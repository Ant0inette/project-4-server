from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/dreams/', include('dreams.urls')),
    path('api/auth/', include('jwt_auth.urls'))
]
