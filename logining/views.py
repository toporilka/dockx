from django.shortcuts import render
from rest_framework import viewsets

from logining.models import User, Client
from logining.serializers import UserSerializer, ClientSerializer
# Create your views here.
# ----------------api--------------------
class UserControllesApi(viewsets.ModelViewSet):
     queryset = User.objects.all()
     serializer_class = UserSerializer



class ClientControllesApi(viewsets.ModelViewSet):
     queryset = Client.objects.all()
     serializer_class = ClientSerializer
