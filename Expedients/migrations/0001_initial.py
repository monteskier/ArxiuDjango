# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expedient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('numexp', models.CharField(max_length=50)),
                ('observacions', models.CharField(max_length=200, null=True)),
                ('estat', models.CharField(max_length=15, default='Disponible', choices=[('Prestat', 'Prestat'), ('Disponible', 'Disponible')])),
            ],
        ),
        migrations.CreateModel(
            name='Fitxa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('codi', models.CharField(max_length=100, default=0)),
                ('data_pub', models.DateTimeField(verbose_name='data de publicacio')),
                ('TAD', models.CharField(max_length=200, null=True)),
                ('ubicacio', models.CharField(max_length=200)),
                ('detall', models.TextField(max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipologia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('codi', models.CharField(max_length=20, default=0)),
                ('concepte', models.CharField(max_length=200)),
                ('data_creacio', models.DateTimeField(auto_now=True)),
                ('data_pub', models.DateTimeField(verbose_name='data de publicacio')),
            ],
        ),
        migrations.AddField(
            model_name='fitxa',
            name='tipus',
            field=models.ForeignKey(related_name='tipologia', to='Expedients.Tipologia'),
        ),
        migrations.AddField(
            model_name='expedient',
            name='fitxa',
            field=models.ForeignKey(related_name='fitxa', to='Expedients.Fitxa'),
        ),
    ]
