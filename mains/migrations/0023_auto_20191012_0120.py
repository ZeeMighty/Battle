# Generated by Django 2.2.4 on 2019-10-11 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mains', '0022_auto_20191012_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mains.date', verbose_name='event_date'),
        ),
    ]
