from django.db import models
from django.contrib.auth.models import AbstractUser


def profile_image_store(instance, filename):
    return f'profile/{instance.username}/{filename}'


class User(AbstractUser):
    age = models.IntegerField(default=18)
    profile_image = models.ImageField(upload_to=profile_image_store, default='profile/default.png')

    def __str__(self):
        return self.username


class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    experience = models.IntegerField()

    def __str__(self):
        return self.user.username


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    tutors = models.ManyToManyField(Tutor, related_name='students', null=True, blank=True)

    @staticmethod
    def update_tutors(sender, instance, action, pk_set, **kwargs):
        if action == 'post_add':
            for tutor_id in pk_set:
                tutor = Tutor.objects.get(pk=tutor_id)
                tutor.students.add(instance)
        elif action == 'post_remove':
            for tutor_id in pk_set:
                tutor = Tutor.objects.get(pk=tutor_id)
                tutor.students.remove(instance)

    def __str__(self):
        return self.user.username
