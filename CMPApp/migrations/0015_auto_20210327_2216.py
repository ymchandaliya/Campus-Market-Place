# Generated by Django 2.2.6 on 2021-03-27 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CMPApp', '0014_auto_20210327_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestedresources',
            name='don',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='requestedresources',
            name='res',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CMPApp.Resource'),
        ),
    ]
