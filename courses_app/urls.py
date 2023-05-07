from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import LanguageViewSet, CourseViewSet

router = DefaultRouter()
router.register('language', LanguageViewSet)
router.register('course', CourseViewSet)


urlpatterns = [
    path('viewset/', include(router.urls))
]
