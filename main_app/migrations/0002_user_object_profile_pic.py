# Generated by Django 4.0.5 on 2022-06-22 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_object',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
