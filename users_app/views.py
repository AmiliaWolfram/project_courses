from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

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


class StudentVoteAPIView(APIView):
    def get(self, request, student_id):
        student = Student.objects.get(pk=student_id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def post(self, request, student_id):
        student = Student.objects.get(pk=student_id)
        serializer = StudentSerializer(student)

        tutor_id = request.data.get('tutor_id')
        tutor = Tutor.objects.get(pk=tutor_id)
        student.vote_for_teacher(tutor)
        serializer = StudentSerializer(student)

        return Response(serializer.data)


class RegistrationTutorRequestAPIView(generics.CreateAPIView):
    queryset = Tutor.objects.all()
    serializer_class = TutorRegisterSerializer
