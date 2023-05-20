from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users_app.models import Tutor
from courses_app.models import Course, Language
from courses_app.serializers import CourseSerializer, LanguageSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, request):
        language = request.data.get('language')
        level = request.data.get('level')
        students = request.data.get('students')
        date_started = request.data.get('date_started')
        duration = request.data.get('duration')
        date_ended = request.data.get('date_ended')
        tutor_id = request.data.get('tutor_id')

        tutor = None
        if tutor_id:
            tutor = get_object_or_404(Tutor, id=tutor_id)

        course = Course(language=language, level=level, students=students, date_started=date_started, duration=duration, date_ended=date_ended)
        course.save()

        serializer = CourseSerializer(course)

        return Response(serializer.data)


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsAuthenticated]
