from rest_framework.serializers import ModelSerializer
from .models import Teebox

class TeeboxSerializer(ModelSerializer):
    class Meta:
        model = Teebox
        fields = ['id', 'user', 'course', 'color1', 'color2']