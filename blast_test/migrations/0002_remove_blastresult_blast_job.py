# Generated by Django 3.1.3 on 2020-11-29 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blast_test', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blastresult',
            name='blast_job',
        ),
    ]
