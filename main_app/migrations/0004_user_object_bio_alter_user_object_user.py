# Generated by Django 4.0.5 on 2022-06-23 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0003_alter_user_object_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_object',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user_object',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
