# Generated by Django 3.2.17 on 2023-03-15 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0017_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
