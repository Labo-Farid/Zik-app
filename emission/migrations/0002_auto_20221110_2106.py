# Generated by Django 2.2.14 on 2022-11-10 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emission', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emissionpodcast',
            name='thumbnail',
            field=models.ImageField(default='emission.JPG', upload_to='Emission/emission_podcasts_images'),
        ),
        migrations.AddField(
            model_name='emissionvideo',
            name='thumbnail',
            field=models.ImageField(default='emission.JPG', upload_to='Emission/emission_videos_images'),
        ),
    ]