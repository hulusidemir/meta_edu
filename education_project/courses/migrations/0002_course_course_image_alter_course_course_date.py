# Generated by Django 4.0.2 on 2022-03-01 02:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_image',
            field=models.ImageField(blank=True, default='no_image.png', upload_to='images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
