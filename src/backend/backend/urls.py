"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('ForumApp.urls')),
    path('api/', include('AnnouncementApp.urls')),
    path('api/', include('dbint.urls')),
    path('api/', include('LoginApp.urls')),
    path('api/', include('ProfileApp.urls')),
    path('api/', include('UniInfoApp.urls')),
    path('api/', include('FileAnalyzeApp.urls')),
    path('api/', include('PlacementApp.urls')),
    path(r'api/auth/', include('knox.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

