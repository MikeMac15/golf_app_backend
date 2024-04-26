from django.urls import path
from .views import User_Course_Tees

urlpatterns = [
    path('<int:pk>/', User_Course_Tees.as_view(), name='teeinfo')
]
