from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets

from .models import User, Tutor, Student
from .serializers import StudentRegisterSerializer


class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = StudentRegisterSerializer
