from rest_framework import serializers, generics
from rest_framework.exceptions import ValidationError

from django.contrib.auth import get_user_model

from users_app.models import User, Tutor, Student
from django.conf import settings

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class StudentRegisterSerializer(serializers.ModelSerializer):
    tutors = serializers.PrimaryKeyRelatedField(many=True, queryset=Tutor.objects.all())
    password = serializers.CharField(max_length=20, write_only=True)
    password2 = serializers.CharField(max_length=20, write_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "password2",
                  "first_name", "last_name", "profile_image", "age", "tutors"]

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords don't match")
        if len(data['password']) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters")
        if data['password'].isdigit():
            raise serializers.ValidationError("Password must contain letters")
        if not any(char.isupper() for char in data['password']) or not any(char.islower() for char in data['password']):
            raise serializers.ValidationError("Password must contain both uppercase and lowercase letters")
        return data

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            age=validated_data['age']
        )
        profile_image = validated_data.get('profile_image')
        if profile_image:
            user.profile_image = profile_image
        user.set_password(validated_data['password'])
        user.save()
        try:
            student = Student.objects.create(user=user)
        except Exception as e:
            user.delete()
            raise e
        else:
            student.username = user.username
            student.profile_image = user.profile_image
            student.age = user.age
        return student


class TutorRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=20, write_only=True)
    password2 = serializers.CharField(max_length=20, write_only=True)
    experience = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ["username", "password", "password2",
                  "first_name", "last_name", "profile_image", "age", "experience"]

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords don't match")
        if len(data['password']) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters")
        if data['password'].isdigit():
            raise serializers.ValidationError("Password must contain letters")
        if not any(char.isupper() for char in data['password']) or not any(char.islower() for char in data['password']):
            raise serializers.ValidationError("Password must contain both uppercase and lowercase letters")
        return data

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            age=validated_data['age']
        )
        profile_image = validated_data.get('profile_image')
        if profile_image:
            user.profile_image = profile_image
        user.set_password(validated_data['password'])
        user.save()
        try:
            tutor = Tutor.objects.create(user=user, experience=validated_data['experience'])
        except Exception as e:
            user.delete()
            raise e
        else:
            tutor.username = user.username
            tutor.profile_image = user.profile_image
            tutor.age = user.age
        return tutor

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
