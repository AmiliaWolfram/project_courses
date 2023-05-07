from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django.contrib.auth import get_user_model

from users_app.models import User, Tutor, Student


class StudentRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=20, write_only=True)
    password2 = serializers.CharField(max_length=20, write_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "password2",
                  "first_name", "last_name", "profile_image", "age"]

    def validate(self, data):
        if data['password'] != data['password2']:
            raise ValidationError("Passwords don't match")
        return data

    def validate_quantity(self, data):
        if len(data['password']) < 8:
            raise ValidationError("Password must be at least 8 characters")
        return data

    def validate_isdigit(self, data):
        if data['password'].isdigit():
            raise ValidationError("Password must contain ABC...")

    def validate_AbCd(self, data):
        for i in data['password']:
            if i.isupper() and i.islower():
                return data
            else:
                raise ValidationError("Where is A and b?")

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
        for i in USER_CHOICES:
            if i == 'Tutor':
                try:
                    tutor = Tutor.objects.create(
                        user=user,
                        experience=validated_data['experience']
                    )
                except Exception as e:
                    user.delete()
                    raise e
                else:
                    tutor.username = user.username
                    tutor.profile_image = user.profile_image
                return tutor
            elif i == 'Student':
                try:
                    student = Student.objects.create(
                        user=user
                    )
                except Exception as e:
                    user.delete()
                    raise e
                else:
                    student.username = user.username
                    student.profile_image = user.profile_image
                return student
