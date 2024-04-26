from django.urls import path
from .views import User_Courses, Delete_Course

urlpatterns = [
    path('user-courses/', User_Courses.as_view(), name='user-courses'),
    path('user-courses/<int:pk>/', Delete_Course.as_view(), name='delete-course')
]
