# Generated by Django 2.2.5 on 2020-01-28 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app5', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='profile_pics',
            field=models.ImageField(blank=True, upload_to='profile_pic'),
        ),
    ]
