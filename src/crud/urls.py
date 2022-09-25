from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('office/', include('office.urls')),
    path('auth/', include('auth_app.urls')),
    path('cbv/', include('cbv_app.urls')),
]
