# Generated by Django 2.2.6 on 2021-03-21 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMPApp', '0008_auto_20210321_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='enroll',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='lname',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
