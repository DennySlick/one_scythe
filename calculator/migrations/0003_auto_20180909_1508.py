# Generated by Django 2.1.1 on 2018-09-09 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_auto_20180908_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='loses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='wins',
            field=models.IntegerField(default=0),
        ),
    ]
