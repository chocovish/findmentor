from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth import login,logout
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

from .utilities import linkedin_api
from .models import Category
from .serializers import CategorySerializer,UserSerializer


from .serializers import UserSerializer
# Create your views here.

class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserByCat(APIView):
    def get(self,request):
        cat = request.GET.get('cat')
        qs = User.objects.filter(user_cat=cat)
        return Response(UserSerializer(qs).data, status=200)

def handleloginlogin(request):
    code = request.GET.get("code","")
    profile = linkedin_api(code)
    user = User.objects.filter(email=profile['email'])
    if user:
        user = user[0]
        user.dp = profile['dp']
        user.save()
        login(request,user)
        return HttpResponseRedirect("http://localhost:8080/")
    else:
        user = User.objects.create(email=profile['email'],first_name=profile['first_name'],last_name=profile['last_name'],l_id=profile['linkedin_id'],dp=profile['dp'])
        login(request,user)
        return HttpResponseRedirect("http://localhost:8080/")

class Logout(APIView):
    def get(self, request, format=None):
        if self.request.user.is_authenticated:
            logout(request)
            return Response(status=200)
        return Response(status=201)


def linkedin(request):
    return render(request,'linkedin.html')


class CategoryList(ListAPIView):
    queryset= Category.objects.all()
    serializer_class = CategorySerializer

class GetUser(APIView):
    def get(self,request):
        u = request.user
        if u.is_authenticated:
            u = UserSerializer(u).data
            return Response(u)
        return Response({'msg':"You are not logged in"})

def home(request):
    return render(request,'index.html')