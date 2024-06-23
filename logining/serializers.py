from rest_framework import serializers
from .models import User, Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta():
        model = Client
        fields = ['name_client','second_name_client','id_user','status']

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ['id_user','email_user','password_user','tag_user']
