# Generated by Django 2.2.6 on 2021-04-06 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMPApp', '0018_newrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=50)),
                ('subject', models.CharField(blank=True, max_length=50)),
                ('suggestion', models.TextField(default='')),
            ],
        ),
    ]
