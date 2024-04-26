from django.urls import path
from .views import Tee_Specific_Holes

urlpatterns = [
    path('<int:pk>/', Tee_Specific_Holes.as_view(), name='holeinfo')
]
