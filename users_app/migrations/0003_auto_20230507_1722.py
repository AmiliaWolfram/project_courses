# Generated by Django 3.2 on 2023-05-07 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0002_auto_20230507_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='tutors',
            field=models.ManyToManyField(blank=True, null=True, related_name='students', to='users_app.Tutor'),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=18),
        ),
    ]