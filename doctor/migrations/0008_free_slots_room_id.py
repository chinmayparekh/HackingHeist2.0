# Generated by Django 4.0.2 on 2022-06-26 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0007_alter_free_slots_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='free_slots',
            name='room_id',
            field=models.CharField(default='', max_length=6),
        ),
    ]
