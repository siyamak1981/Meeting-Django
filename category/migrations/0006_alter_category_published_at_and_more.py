# Generated by Django 4.0.1 on 2022-02-13 07:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_alter_category_published_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 13, 7, 51, 24, 588535, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 13, 7, 51, 24, 588535, tzinfo=utc)),
        ),
    ]
