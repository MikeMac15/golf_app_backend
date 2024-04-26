from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT,
    HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN
)
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Club
from .serializers import ClubSerializer
# Create your views here.
class User_Clubs(APIView):
    authentication_classes= [TokenAuthentication]
    permission_classes= [IsAuthenticated]

    def get(self,request):
        user = request.user
        clubs = Club.objects.get_user_clubs(user)
        serializer = ClubSerializer(clubs, many = True)

        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request):
        user = request.user
        data = request.data

        data['user'] = user.id

        serializer = ClubSerializer(data=data)

        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        
        # serializer = ClubSerializer(data=request.data)

        # if serializer.is_valid():
        #     serializer.save(user=request.user)
        #     return Response(serializer.data, status=HTTP_201_CREATED)
        # return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

