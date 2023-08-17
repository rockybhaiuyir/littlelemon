# Generated by Django 4.1.5 on 2023-01-29 21:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookingAPI', '0002_remove_booking_peoople_booking_people'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='people',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(300)]),
        ),
    ]