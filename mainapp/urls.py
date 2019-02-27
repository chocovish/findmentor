from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('user',views.UserViewSet)



urlpatterns = [
    path('login/linkedin/callback/',views.handleloginlogin),
    path('linkedin/',views.linkedin),
    path('categorylist/',views.CategoryList.as_view()),
    path('getuser/',views.GetUser.as_view()),
    path('',views.home),
]