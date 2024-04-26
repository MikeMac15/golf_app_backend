from django.db import models
from user_app.models import GolfUser
from course_app.models import Course
# Create your models here.
class User_Tee_Manager(models.Manager):
    def get_user_tees(self, user, course):
        return self.filter(user=user, course=course)
    
class Teebox(models.Model):
    user = models.ForeignKey(GolfUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    color1 = models.CharField(max_length=10)
    color2 = models.CharField(max_length=10, null=True, blank=True)

    objects = User_Tee_Manager()

    def __str__(self):
        return f'{self.color1}, {self.color2}, {self.pk}'