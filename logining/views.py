from django.shortcuts import render
from django.http.response import JsonResponse

from logining.models import User, Client
from logining.serializers import UserSerializer, ClientSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import viewsets


# ----------------api--------------------
class UserControllesApi(viewsets.ModelViewSet):
     queryset = User.objects.all()
     serializer_class = UserSerializer

class ClientControllesApi(viewsets.ModelViewSet):
     queryset = Client.objects.all()
     serializer_class = ClientSerializer

# ---------------views-------------------
@api_view(['POST','GET','DELETE'])
def req_method(request):
     if request.method == 'GET':
          users = User.objects.all()

          email = request.query_params.get('email_user', None)
          if email is not None:
               email = email.filter(email_icontains = email)
          
          users_serializer = UserSerializer(users, many = True)
          return JsonResponse(users_serializer.data, safe=False)
     
     elif request.method == 'POST':
          user_data = JSONParser().parse(request)
          user_serializer = UserSerializer(data=user_data)
          if user_serializer.is_valid():
               user_serializer.save()
               return JsonResponse(user_serializer.data, status = status.HTTP_201_CREATED)
          return JsonResponse(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
     elif request.method == 'DELETE':
          count = User.objects.all().delete()
          return JsonResponse({'message': '{} User were deleted succefuly'.format(count[0])}, status = status.HTTP_204_NO_CONTENT)


