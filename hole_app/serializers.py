from rest_framework.serializers import ModelSerializer
from .models import Hole

class HoleSerializer(ModelSerializer):
    class Meta:
        model = Hole
        fields = ['id','user','teebox','number','par','distance','color']