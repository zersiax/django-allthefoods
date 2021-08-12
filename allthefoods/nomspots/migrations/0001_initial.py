# Generated by Django 3.1.1 on 2021-08-11 00:56

import autoslug.fields
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nomspot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='Name of food place')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True, verbose_name='Nomspot address')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('goodness', models.CharField(choices=[('unspecified', 'Unspecified')], default='unspecified', max_length=20, verbose_name='How good the place is')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
