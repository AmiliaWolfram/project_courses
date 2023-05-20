from rest_framework import serializers

from courses_app.models import Course, Language


class CourseSerializer(serializers.ModelSerializer):
    tutor = serializers.ReadOnlyField(source='tutor.username')

    class Meta:
        model = Course
        exclude = ['date_ended']


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'
