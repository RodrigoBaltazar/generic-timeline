# Generated by Django 4.0 on 2022-01-07 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0002_video_media_alter_video_approved_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='media',
            field=models.FileField(upload_to='media/'),
        ),
    ]