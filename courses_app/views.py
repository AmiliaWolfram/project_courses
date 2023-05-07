from django.shortcuts import render
from rest_framework import viewsets

from courses_app.models import Course, Language
from courses_app.serializers import CourseSerializer, LanguageSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
