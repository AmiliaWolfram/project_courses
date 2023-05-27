from django.urls import path, include

from . import views

urlpatterns = [
    path('register/student/', views.UserStudentRegisterAPIView.as_view()),
    path('register/tutor/', views.RegistrationTutorRequestAPIView.as_view()),
    path('list/tutors/', views.TutorViewSet.as_view()),
    path('list/students/', views.StudentViewSet.as_view()),
    path('auth', include('rest_framework.urls')),
]
