# Generated by Django 4.1.1 on 2022-11-25 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='boards',
            name='is_anon',
            field=models.BooleanField(default=False),
        ),
    ]
