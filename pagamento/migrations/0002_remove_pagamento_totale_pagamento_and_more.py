# Generated by Django 4.1 on 2023-06-09 13:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagamento', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagamento',
            name='totale_pagamento',
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='data_pagamento',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 9, 15, 20, 38, 52863)),
        ),
    ]
