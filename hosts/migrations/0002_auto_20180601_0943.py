# Generated by Django 2.0.4 on 2018-06-01 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostmodel',
            name='description',
            field=models.CharField(blank=True, max_length=128, verbose_name='Description of Host'),
        ),
    ]
