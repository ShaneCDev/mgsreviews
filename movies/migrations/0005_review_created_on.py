# Generated by Django 3.2.17 on 2023-02-22 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20230221_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
