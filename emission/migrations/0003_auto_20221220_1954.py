# Generated by Django 2.2.14 on 2022-12-20 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emission', '0002_auto_20221110_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emissionvideo',
            name='thumbnail',
            field=models.ImageField(default='emission.jpg', upload_to='Emission/emission_videos_images'),
        ),
    ]