from django.urls import include, path
from rest_framework import routers

from recall.views import CommentViewSet

router = routers.DefaultRouter()
router.register('comments', CommentViewSet)

urlpatterns = [
    path('viewset/', include(router.urls)),
]
