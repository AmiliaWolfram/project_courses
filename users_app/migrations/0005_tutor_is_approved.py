# Generated by Django 3.2 on 2023-05-18 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0004_auto_20230518_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]