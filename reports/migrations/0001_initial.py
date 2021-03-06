# Generated by Django 2.0.4 on 2018-07-25 07:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
        ('scans', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=64, verbose_name='Name of Report')),
                ('file', models.FileField(upload_to='', verbose_name='File report')),
                ('dateUpdate', models.DateTimeField(auto_now=True)),
                ('createBy', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('scanProject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.ScanProjectModel')),
                ('scanTask', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='scans.ScanTaskModel')),
            ],
        ),
    ]
