# Generated by Django 3.0.8 on 2020-07-28 05:42

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200728_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roi_divided',
            name='geom',
            field=django.contrib.gis.db.models.fields.GeometryCollectionField(srid=4326),
        ),
        migrations.AlterField(
            model_name='roi_divided',
            name='name',
            field=models.CharField(default='Null', max_length=100, null=True),
        ),
    ]