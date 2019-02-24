from django.shortcuts import render,HttpResponse
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth import login
from rest_framework.generics import ListAPIView
import requests

from .utilities import linkedin_api
from .models import Category
from .serializers import CategorySerializer,UserSerializer



from .serializers import UserSerializer
# Create your views here.

class UserViewSet(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def handleloginlogin(request):
    code = request.GET.get("code","")
    profile = linkedin_api(code)
    user = User.objects.filter(email=profile['email'])
    if user:
        user = user[0]
        login(request,user)
        return HttpResponse("You are logged in: " + request.user.username)
    else:
        user = User.objects.create(email=profile['email'],first_name=profile['first_name'],last_name=profile['last_name'],l_id=profile['linkedin_id'])
        return HttpResponse("User Created")


def linkedin(request):
    return render(request,'linkedin.html')


class CategoryList(ListAPIView):
    queryset= Category.objects.all()
    serializer_class = CategorySerializer