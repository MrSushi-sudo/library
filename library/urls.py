from django.contrib import admin
from django.urls import path, include
from library_catalog.views import redirect_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_view),
    path('api/', include('library_catalog.urls')),
]
