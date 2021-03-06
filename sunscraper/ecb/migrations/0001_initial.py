# Generated by Django 2.0.5 on 2018-05-15 07:33

import django.contrib.postgres.indexes
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('code', models.CharField(db_index=True, max_length=3, unique=True)),
                ('rss_link', models.URLField()),
            ],
            options={
                'verbose_name': 'curency',
                'verbose_name_plural': 'currencies',
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('value', models.DecimalField(decimal_places=4, max_digits=12)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecb.Currency')),
            ],
        ),
        migrations.AddIndex(
            model_name='rate',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['date'], name='ecb_rate_date_387878_brin'),
        ),
    ]
