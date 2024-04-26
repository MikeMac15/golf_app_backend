from rest_framework.serializers import ModelSerializer
from .models import Club

class ClubSerializer(ModelSerializer):
    class Meta:
        model = Club
        fields = ['id', 'user', 'symbol', 'brand', 'club_type', 'hidden']
