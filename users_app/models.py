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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    students = models.ManyToManyField('Student', related_name='tutor_set', related_query_name='tutor', blank=True)
    experience = models.IntegerField()
    votes = models.IntegerField(default=0)
    is_approved = models.BooleanField(default=False)

    @staticmethod
    def update_students(sender, instance, action, pk_set, **kwargs):
        if action == 'post_add':
            for student_id in pk_set:
                student = Student.objects.get(pk=student_id)
                student.tutors.add(instance)
        elif action == 'post_remove':
            for student_id in pk_set:
                student = Student.objects.get(pk=student_id)
                student.tutors.remove(instance)

    def __str__(self):
        return self.user.username

    def increment_votes(self):
        self.votes += 1
        self.save()


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tutors = models.ManyToManyField(Tutor, related_name='student_set', related_query_name='student', blank=True)

    # voted_tutor = models.ForeignKey(Tutor, on_delete=models.SET_NULL, null=True, blank=True)
    voted_tutor = models.ForeignKey(Tutor, on_delete=models.SET_NULL, null=True, blank=True, related_name='votes_received')

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

    def vote_for_tutor(self, teacher):
        if self.voted_tutor is not None:
            self.voted_tutor.votes -= 1
            self.voted_tutor.save()
        # self.voted_teacher = teacher
        self.voted_tutor = teacher  # Updated field name
        teacher.increment_votes()
        self.save()
