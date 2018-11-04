# Generated by Django 2.1.2 on 2018-11-01 07:25

import django.core.files.storage
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submit', '0011_auto_20181027_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submitmodel',
            name='fileSubmitted',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage('C:\\Users\\tuank\\PycharmProjects\\VulnerablititesManagement\\files_data\\imported_file'), upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['zip'])], verbose_name='File attachment'),
        ),
    ]
