# Generated by Django 4.0 on 2022-01-07 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0004_alter_video_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='approved',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
