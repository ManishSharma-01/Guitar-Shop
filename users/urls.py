from django.contrib import admin
from django.urls import path, include
from users import views


urlpatterns = [
    path("register_user",views.register_name, name='register_user'),
    path("login_user",views.login_user, name='login_user'),
    path("show_user_details", views.show_user_details, name="show_user_details"),
    path("update_user/<id>",views.update_user, name='update_user'),
    path("logout",views.logout, name='logout'),
    path("update_password/<id>",views.update_password, name='update_password'),
    path("delete_user/<id>",views.delete_user, name='delete_user'),
]