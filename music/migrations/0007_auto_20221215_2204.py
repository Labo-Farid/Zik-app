# Generated by Django 2.2.14 on 2022-12-15 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_auto_20221208_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='music',
            field=models.ManyToManyField(to='music.PlaylistAudio'),
        ),
    ]
