from django.urls import path
from .views import User_Clubs

urlpatterns = [
    path('', User_Clubs.as_view(), name='user-clubs')
]
