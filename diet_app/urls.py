from django.urls import path

from django.contrib import admin
from diet_app.views import *


urlpatterns = [
    path("", index, name="index"),
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("nut/", nut, name="diet_plan"),
    path("diet_plan/", diet_plan, name="diet_plan"),
]
