# Generated by Django 2.2.14 on 2022-11-10 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('country', django_countries.fields.CountryField(default='togo', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('type', models.CharField(choices=[('free', 'Free'), ('premium', 'Premium')], default='free', max_length=20)),
                ('price', models.FloatField(blank=True, null=True)),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('audio', models.FileField(upload_to='Musics/audios')),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='Musics/images')),
                ('is_on_top', models.BooleanField(default=False)),
                ('is_popular', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=20)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('artist', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='music.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='MusicCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MusicTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('type', models.CharField(choices=[('free', 'Free'), ('premium', 'Premium')], default='free', max_length=20)),
                ('price', models.FloatField(blank=True, null=True)),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='Musics/playlist/images')),
                ('is_on_top', models.BooleanField(default=False)),
                ('is_popular', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=20)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('music', models.ManyToManyField(to='music.Music')),
                ('playlist_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.MusicCategory')),
                ('tags', models.ManyToManyField(to='music.MusicTags')),
            ],
        ),
        migrations.CreateModel(
            name='OrderMusic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('music', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Music')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MusicCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_code', models.CharField(blank=True, max_length=20, null=True)),
                ('ordered_date', models.DateTimeField()),
                ('ordered', models.BooleanField(default=False)),
                ('musics', models.ManyToManyField(to='music.Music')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='music',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.MusicCategory'),
        ),
        migrations.AddField(
            model_name='music',
            name='tags',
            field=models.ManyToManyField(to='music.MusicTags'),
        ),
        migrations.CreateModel(
            name='AlbumAudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('audio', models.FileField(upload_to='Musics/albums/albums_audios')),
                ('image', models.ImageField(default='album.JPG', upload_to='Musics/albums/albums_audios_images')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('artist', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='music.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('zip_file', models.FileField(default='', upload_to='Music/albums/albums_zip_files')),
                ('type', models.CharField(choices=[('free', 'Free'), ('premium', 'Premium')], default='free', max_length=20)),
                ('price', models.FloatField(blank=True, null=True)),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='Music/albums/albums_images')),
                ('is_on_top', models.BooleanField(default=False)),
                ('is_popular', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=20)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('audio', models.ManyToManyField(to='music.AlbumAudio')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.MusicCategory')),
                ('tags', models.ManyToManyField(to='music.MusicTags')),
            ],
        ),
    ]
