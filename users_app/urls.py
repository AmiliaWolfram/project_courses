from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('register/student/', views.UserStudentRegisterAPIView.as_view()),
    path('register/tutor/', views.RegistrationTutorRequestAPIView.as_view()),
    path('list/tutors/', views.TutorViewSet.as_view()),
    path('list/students/', views.StudentViewSet.as_view()),
    path('token/', obtain_auth_token),
    path('auth', include('rest_framework.urls')),
]
