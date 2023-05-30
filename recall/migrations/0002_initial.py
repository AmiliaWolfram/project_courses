# Generated by Django 4.2 on 2023-05-30 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users_app', '0001_initial'),
        ('recall', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users_app.student'),
        ),
        migrations.AddField(
            model_name='comment',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users_app.tutor'),
        ),
    ]
