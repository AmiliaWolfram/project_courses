from rest_framework import generics, status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from courses_app.permissions import IsStudent
from .models import User, Tutor, Student
from .serializers import StudentRegisterSerializer, TutorRegisterSerializer, \
    TutorSerializer, StudentSerializer, VoteForTutorSerializer


class UserStudentRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = StudentRegisterSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]


class UserTutorRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = TutorRegisterSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]


class TutorViewSet(generics.ListAPIView):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]


class StudentViewSet(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]


class RegistrationTutorRequestAPIView(generics.CreateAPIView):
    queryset = Tutor.objects.all()
    serializer_class = TutorRegisterSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]


class VoteForTutorViewSet(ViewSet):
    serializer_class = VoteForTutorSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsStudent, ]

    def create(self, request, *args, **kwargs):
        student = self.get_student_object(request.user)
        tutor_id = request.data.get('tutor_id')

        if tutor_id is not None:
            tutor = get_object_or_404(Tutor, id=tutor_id)
            student.vote_for_tutor(tutor)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get_student_object(self, user):
        student = get_object_or_404(Student, user=user)
        return student
