# Generated by Django 3.0.4 on 2020-07-18 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IsroBackend', '0003_imagemaskdetails_timetaken'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagemaskdetails',
            old_name='timeTaken',
            new_name='timeTakenCPU',
        ),
        migrations.AddField(
            model_name='imagemaskdetails',
            name='timeTakenHuman',
            field=models.FloatField(null=True),
        ),
    ]
