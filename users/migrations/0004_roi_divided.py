# Generated by Django 3.0.8 on 2020-07-28 04:41

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_roi'),
    ]

    operations = [
        migrations.CreateModel(
            name='ROI_DIVIDED',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.BigIntegerField(blank=True, null=True)),
                ('name', models.CharField(default='Null', max_length=100)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'ROI_DIVIDED',
            },
        ),
    ]
