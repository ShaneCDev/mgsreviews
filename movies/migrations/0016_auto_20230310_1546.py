# Generated by Django 3.2.17 on 2023-03-10 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0015_game_synopsis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='carousel_image',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='carousel_image',
        ),
        migrations.RemoveField(
            model_name='show',
            name='carousel_image',
        ),
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='show',
            name='description',
            field=models.TextField(max_length=3000),
        ),
    ]
