# Generated by Django 4.0.5 on 2022-06-23 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_user_object_bio_alter_user_object_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_object',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
