# Generated by Django 2.0.6 on 2018-11-26 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faceRecognitionWebsite', '0006_auto_20181126_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='groups_ids',
        ),
        migrations.AddField(
            model_name='subject',
            name='groups',
            field=models.ManyToManyField(to='faceRecognitionWebsite.Group', verbose_name='list of groups'),
        ),
    ]
