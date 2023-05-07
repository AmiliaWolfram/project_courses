from rest_framework import serializers

from courses_app.models import Course, Language


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        exclude = ['date_ended']


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'
