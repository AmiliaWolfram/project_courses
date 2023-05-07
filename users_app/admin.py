from django.contrib import admin

from users_app.models import Student, Tutor, User

admin.site.register(Student)
admin.site.register(User)
admin.site.register(Tutor)
