from django.db import models

from users_app.models import Tutor, Student


class Comment(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    text = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.tutor.user.username}'
