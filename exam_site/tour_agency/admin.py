from django.contrib import admin
from .models import Client, Tour, Application
#from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#from django.contrib.auth.models import User

# class UserAdmin(BaseUserAdmin):
#     list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
admin.site.register(Client)
admin.site.register(Tour)
admin.site.register(Application)
