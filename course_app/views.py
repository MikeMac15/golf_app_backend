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
from .models import Course
from .serializers import CourseSerializer
# Create your views here.

class User_Courses(APIView):
    authentication_classes= [TokenAuthentication]
    permission_classes= [IsAuthenticated]

    def get(self, request):
        user = request.user
        golf_courses = Course.objects.get_user_courses(user)
        serializer = CourseSerializer(golf_courses, many = True)

        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        user = request.user
        data = request.data

        data['user'] = user.id

        serializer = CourseSerializer(data=data)

        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class Delete_Course(APIView):
    authentication_classes= [TokenAuthentication]
    permission_classes= [IsAuthenticated]

    def delete(self, request, pk):
        user = request.user
        course = get_object_or_404(Course, pk=pk, user=user)

        if course.user != user:
            return Response({'detail': 'Permission Denied. This course does not belong to the user.'}, status=HTTP_403_FORBIDDEN)
        course.delete()
        return Response(status=HTTP_204_NO_CONTENT)