# Generated by Django 2.2.4 on 2019-10-04 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mains', '0018_event_event_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_date',
        ),
    ]
