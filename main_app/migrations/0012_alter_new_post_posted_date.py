# Generated by Django 4.0.5 on 2022-06-25 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_new_post_posted_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_post',
            name='posted_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
