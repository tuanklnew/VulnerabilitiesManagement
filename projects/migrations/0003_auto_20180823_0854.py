# Generated by Django 2.0.4 on 2018-08-23 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20180725_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scanprojectmodel',
            name='description',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Description of scanning project'),
        ),
    ]
