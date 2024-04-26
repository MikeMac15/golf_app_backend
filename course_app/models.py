from django.db import models
from user_app.models import GolfUser

# Create your models here.
class User_Courses_Manager(models.Manager):
    def get_user_courses(self, user):
        return self.filter(user=user)

class Course(models.Model):
    user = models.ForeignKey(GolfUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    objects = User_Courses_Manager()

    def __str__(self):
        return f'{self.name}'
    