# Generated by Django 5.0 on 2023-12-19 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='sex',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='room',
            field=models.ManyToManyField(blank=True, to='hotel.person'),
        ),
    ]
