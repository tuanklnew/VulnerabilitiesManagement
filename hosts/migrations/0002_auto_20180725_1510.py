# Generated by Django 2.0.4 on 2018-07-25 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostmodel',
            name='hostName',
            field=models.CharField(max_length=128),
        ),
    ]
