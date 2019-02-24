from rest_framework import serializers
from .views import User
from .models import Category

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','usertype','user_cat','first_name','last_name','headline','l_id','dp']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = []
