# Generated by Django 3.2.6 on 2021-08-06 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='is_seminar',
            field=models.BooleanField(default=False, verbose_name='Is Event a Seminar'),
        ),
    ]