from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from logining.models import User, Client
from logining.serializers import UserSerializer, ClientSerializer


# ----------------api--------------------
class UserControllesApi(viewsets.ModelViewSet):
     queryset = User.objects.all()
     serializer_class = UserSerializer

class ClientControllesApi(viewsets.ModelViewSet):
     queryset = Client.objects.all()
     serializer_class = ClientSerializer

# ---------------views-------------------

