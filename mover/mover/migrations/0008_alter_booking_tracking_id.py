# Generated by Django 4.2.5 on 2023-09-19 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mover', '0007_booking_tracking_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='tracking_id',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
