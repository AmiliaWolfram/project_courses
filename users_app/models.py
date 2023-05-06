from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser

import courses_app.models as courses


class User(AbstractUser):

    def __str__(self):
        return self.username


class Student(User):
    courses = models.ManyToManyField(courses.Course)


class Tutor(User):
    courses = models.ForeignKey(courses.Course, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    experience = models.IntegerField()
