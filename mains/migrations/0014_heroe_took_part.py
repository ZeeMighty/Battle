# Generated by Django 2.1.7 on 2019-06-03 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mains', '0013_auto_20190603_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='heroe',
            name='took_part',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mains.event'),
        ),
    ]
