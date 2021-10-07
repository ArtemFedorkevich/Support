from django.contrib import admin

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('authentication.urls', namespace='authentication')),
    path('api/', include('useractions.urls', namespace='useractions')),
    path('api/', include('staff_part.urls', namespace='staff_part')),
]
