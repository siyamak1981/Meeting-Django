# Generated by Django 3.2.9 on 2022-02-14 12:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_profile_published_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 14, 12, 46, 29, 862791, tzinfo=utc)),
        ),
    ]
