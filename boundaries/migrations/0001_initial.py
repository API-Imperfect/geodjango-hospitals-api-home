# Generated by Django 3.1.7 on 2021-03-28 09:18

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boundary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adm0_en', models.CharField(max_length=254)),
                ('adm0_sw', models.CharField(max_length=254)),
                ('adm0_pcode', models.CharField(max_length=254)),
                ('name', models.CharField(max_length=254, verbose_name='Border Name')),
                ('adm1_rw', models.CharField(max_length=254)),
                ('adm1_pcode', models.CharField(max_length=254)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Boundaries',
            },
        ),
    ]
