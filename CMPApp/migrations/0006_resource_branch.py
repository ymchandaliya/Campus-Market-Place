# Generated by Django 2.2.6 on 2021-03-19 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMPApp', '0005_auto_20210318_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='Branch',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
