# Generated by Django 3.0.8 on 2020-07-28 05:49

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200728_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roi_divided',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
        ),
    ]
