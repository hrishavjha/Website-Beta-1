from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('user.urls')),
    path('discussion/', include('forum.urls')),
    path('search/', include('search.urls')),
]
