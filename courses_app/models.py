from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from datetime import datetime, timedelta

from users_app.models import Tutor, Student


class Language(models.Model):
    denomination = models.CharField(max_length=20)


def date_func(date_started, duration):
    date_ended1 = date_started + timedelta(days=duration)
    return date_ended1


# def get_end_date(date_started, duration):
#     date_ended = date_started + timedelta(months=duration)
#     return datetime.strptime(date_ended, '%Y-%m-%d')


@receiver(post_save, sender=Language)
@receiver(post_delete, sender=Language)
def update_language_field(sender, instance, **kwargs):
    courses = Course.objects.filter(language=instance)
    if not courses.exists():
        return
    if kwargs.get('created', True):
        # Language was added
        courses.update(language=instance)
    else:
        # Language was deleted
        default_language = Language.objects.first()  # Choose a default language to assign to the courses
        courses.update(language=default_language)


class Course(models.Model):
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True)
    tutor = models.ForeignKey(Tutor, on_delete=models.SET_NULL, null=True, blank=True)
    students = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    date_started = models.DateTimeField()
    duration = models.IntegerField()
    date_ended = models.DateTimeField()
