# Generated by Django 2.0.6 on 2018-11-26 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faceRecognitionWebsite', '0005_grade_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='group',
        ),
        migrations.AddField(
            model_name='person',
            name='groups',
            field=models.ManyToManyField(to='faceRecognitionWebsite.Group', verbose_name='list of groups'),
        ),
    ]
