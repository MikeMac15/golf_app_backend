from django.db import models
from user_app.models import GolfUser
# Create your models here.
class User_Club_Manager(models.Manager):
    def get_user_clubs(self,user):
        return self.filter(user=user)
    
class Club(models.Model):
    user = models.ForeignKey(GolfUser, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=6)
    brand = models.CharField(max_length=20)
    club_type = models.CharField(max_length=10)
    hidden = models.BooleanField(default=False)

    objects = User_Club_Manager()

    def __str__(self):
        return f'{self.symbol}: {self.brand}'