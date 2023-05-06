from django.db import models

from django.db import models

from datetime import datetime, timedelta


class Language(models.Model):
    denomination = models.CharField(max_length=20)


def date_func(date_started, duration):
    date_ended1 = date_started + timedelta(days=duration)
    return date_ended1


# def get_end_date(date_started, duration):
#     date_ended = date_started + timedelta(months=duration)
#     return datetime.strptime(date_ended, '%Y-%m-%d')


class Course(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    date_started = models.DateTimeField()
    duration = models.IntegerField()
    date_ended = models.DateTimeField()
