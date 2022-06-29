# Generated by Django 3.2.9 on 2022-02-01 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(help_text='must be unique', max_length=128, unique_for_month='created')),
                ('slug', models.CharField(max_length=128, unique_for_month='created')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'ordering': ['-created'],
            },
        ),
    ]
