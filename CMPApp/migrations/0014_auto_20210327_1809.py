# Generated by Django 2.2.6 on 2021-03-27 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CMPApp', '0013_auto_20210327_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestedresources',
            name='res',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='CMPApp.Resource'),
        ),
    ]
