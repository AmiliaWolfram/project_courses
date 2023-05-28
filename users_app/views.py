from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User, Tutor, Student
from .serializers import StudentRegisterSerializer, TutorRegisterSerializer, \
    TutorSerializer, StudentSerializer
from courses_app.permissions import IsStudentOrTutor


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


class VoteForTutorView(generics.CreateAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsStudentOrTutor, ]

    def create(self, request, *args, **kwargs):
        student = self.get_student_object(request.user)
        teacher_id = request.data.get('teacher_id')

        if teacher_id is not None:
            teacher = get_object_or_404(Tutor, id=teacher_id)
            student.vote_for_tutor(teacher)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get_student_object(self, user):
        student = get_object_or_404(Student, user=user)
        return student
