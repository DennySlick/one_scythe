# Generated by Django 2.1.1 on 2018-09-07 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0007_auto_20180907_1650'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playeringame',
            old_name='difPoints',
            new_name='pts_dif',
        ),
        migrations.RenameField(
            model_name='playeringame',
            old_name='startPoints',
            new_name='pts_start',
        ),
    ]
