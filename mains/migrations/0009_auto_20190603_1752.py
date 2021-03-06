# Generated by Django 2.1.7 on 2019-06-03 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mains', '0008_army'),
    ]

    operations = [
        migrations.CreateModel(
            name='events_has_Army',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('events_idEvents', models.IntegerField()),
                ('Army_idArmy', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='army',
            name='army_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mains.events_has_Army'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mains.events_has_Army'),
        ),
    ]
