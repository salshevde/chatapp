from django.contrib import admin
from django.urls import path
from . import views
app_name = 'users'

urlpatterns = [
    path('',views.profile,name="profile"),
    path('register',views.register_user,name="register"),
    path('login',views.login_user,name="login"),
    path('logout',views.logout_user,name="logout"),
    # path('login',views.login_user,name="login"),

]