# Generated by Django 3.2.9 on 2022-02-02 14:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_published_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 2, 14, 11, 28, 587276, tzinfo=utc)),
        ),
    ]
