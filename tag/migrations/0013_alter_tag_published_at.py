# Generated by Django 4.0.1 on 2022-02-21 20:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0012_alter_tag_published_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='published_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]