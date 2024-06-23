from rest_framework import serializers
from .models import User, Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta():
        model = Client
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = '__all__'
    
