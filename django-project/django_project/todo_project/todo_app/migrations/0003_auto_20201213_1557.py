# Generated by Django 2.2.5 on 2020-12-13 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                
            ],
        ),
    ]
