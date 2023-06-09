"""repair_cafe_item_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from repair_cafe_item_tracker.apps.backend.admin import backend_admin_site

urlpatterns = [
    path('', include(('repair_cafe_item_tracker.apps.frontend.urls', 'frontend'), namespace='repair_cafe_item_tracker.apps.frontend')),
    path('backend/', include(('repair_cafe_item_tracker.apps.backend.urls', 'backend'), namespace='repair_cafe_item_tracker.apps.backend')),
    path('admin/', admin.site.urls),
    path('backendadmin/', backend_admin_site.urls)
]
