from django.db import models
from user_app.models import GolfUser
from teebox_app.models import Teebox
# Create your models here.
class Tee_Specific_Holes_Manager(models.Manager):
    def get_tee_specific_holes_list(self, user, teebox):
        return self.filter(user=user, teebox=teebox)
    
class Hole(models.Model):
    user = models.ForeignKey(GolfUser, on_delete=models.CASCADE)
    teebox = models.ForeignKey(Teebox, on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField()
    par = models.PositiveSmallIntegerField()
    distance = models.PositiveSmallIntegerField()
    color = models.CharField(max_length=10)

    objects = Tee_Specific_Holes_Manager()

    def __str__(self):
        return f'Hole {self.number}, color: {self.color}'