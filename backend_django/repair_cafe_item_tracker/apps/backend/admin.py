from django.contrib import admin
from .models import Item

class BackendAdminSite(admin.AdminSite):
    site_header = "Backend Admin"
    
backend_admin_site = BackendAdminSite(name="backendadmin")
backend_admin_site.register(Item)
