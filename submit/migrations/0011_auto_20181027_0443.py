# Generated by Django 2.1.2 on 2018-10-27 04:43

import django.core.files.storage
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submit', '0010_auto_20181022_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submitmodel',
            name='fileSubmitted',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage('/home/fedora/PythonProject/VulnerablititesManagement/files_data/imported_file'), upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['zip'])], verbose_name='File attachment'),
        ),
    ]
