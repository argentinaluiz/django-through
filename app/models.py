from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User, through='Enrollment')

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.PROTECT)