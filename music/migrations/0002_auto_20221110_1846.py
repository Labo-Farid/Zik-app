# Generated by Django 2.2.14 on 2022-11-10 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]