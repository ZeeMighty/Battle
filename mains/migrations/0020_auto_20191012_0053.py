# Generated by Django 2.2.4 on 2019-10-11 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mains', '0019_remove_event_event_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='date',
            name='date_id',
        ),
        migrations.AddField(
            model_name='event',
            name='event_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mains.date'),
        ),
    ]