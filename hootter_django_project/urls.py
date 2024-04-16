from django.contrib import admin
from django.urls import path, include  # Import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Include core app's URLs for the root path
    path('user_management/', include('user_management.urls')),
    path('public_messages/', include('public_messages.urls'))
]
