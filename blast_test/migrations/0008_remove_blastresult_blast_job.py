# Generated by Django 3.1.3 on 2020-12-01 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blast_test', '0007_auto_20201201_0530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blastresult',
            name='blast_job',
        ),
    ]
