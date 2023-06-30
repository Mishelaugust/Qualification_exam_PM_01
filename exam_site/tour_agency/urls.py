from . import views
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('', views.home, name = 'home'),
    path('logout/', views.logout_user, name = 'logout'),
    path('add_client/', views.add_client, name = 'add_client'),
    path('add_application/', views.add_application, name = 'add_application'),
    path('update_application/<int:pk>', views.update_application, name = 'update_application'),
    path('delete_application/<int:pk>', views.delete_application, name = 'delete_application'),
]
