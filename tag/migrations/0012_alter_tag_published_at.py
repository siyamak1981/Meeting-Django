# Generated by Django 4.0.1 on 2022-02-21 19:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0011_alter_tag_published_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 21, 19, 0, 50, 24225, tzinfo=utc)),
        ),
    ]
