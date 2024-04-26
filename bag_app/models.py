from django.db import models
from user_app.models import GolfUser
from club_app.models import Club
# Create your models here.
class User_Bag_Manager(models.Manager):
    def get_user_bags(self, user):
        return self.filter(user=user)

class Bag(models.Model):
    user = models.ForeignKey(GolfUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    clubs = models.ManyToManyField(Club)
    hidden = models.BooleanField(default=False)

    objects = User_Bag_Manager()

    def __str__(self):
        return f'{self.name}'