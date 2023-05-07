from rest_framework import generics

from .models import User, Tutor, Student
from .serializers import StudentRegisterSerializer, TutorRegisterSerializer, \
    TutorSerializer, StudentSerializer


class UserStudentRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = StudentRegisterSerializer


class UserTutorRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = TutorRegisterSerializer


class TutorViewSet(generics.ListAPIView):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer


class StudentViewSet(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
