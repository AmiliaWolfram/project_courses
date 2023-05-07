from django.urls import path

from . import views

urlpatterns = [
    path('register/student/', views.UserStudentRegisterAPIView.as_view()),
    path('register/tutor/', views.UserTutorRegisterAPIView.as_view()),
    path('list/tutors/', views.TutorViewSet.as_view()),
    path('list/students/', views.StudentViewSet.as_view()),
]
