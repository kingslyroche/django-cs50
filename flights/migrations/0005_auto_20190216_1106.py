# Generated by Django 2.1.7 on 2019-02-16 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='flights',
            field=models.ManyToManyField(blank=True, related_name='passenger', to='flights.Flight'),
        ),
    ]
