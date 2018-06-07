# Generated by Django 2.0.1 on 2018-01-17 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlignmentConsensus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('alignment', models.BinaryField()),
                ('gn_consensus', models.BinaryField(blank=True)),
            ],
        ),
    ]
