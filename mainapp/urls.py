from django.urls import path
from rest_framework import routers
from . import views




urlpatterns = [
    path('login/linkedin/callback/',views.handleloginlogin),
    path('logout/',views.Logout.as_view()),
    path('linkedin/',views.linkedin),
    path('categorylist/',views.CategoryList.as_view()),
    path('getuser/',views.GetUser.as_view()),
    path('allusers/',views.UserList.as_view()),
    path('',views.home),
]
