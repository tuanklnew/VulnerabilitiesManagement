# Generated by Django 2.1.2 on 2018-10-16 16:22

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0011_auto_20181004_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportmodel',
            name='fileReport',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/home/fedora/PythonProject/VulnerablititesManagement/files_data/generated_report'), upload_to='', verbose_name='File report'),
        ),
    ]
