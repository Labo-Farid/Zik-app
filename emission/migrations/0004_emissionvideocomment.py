# Generated by Django 2.2.14 on 2022-12-21 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('emission', '0003_auto_20221220_1954'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmissionVideoComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('emission_video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='emission.EmissionVideo')),
            ],
        ),
    ]