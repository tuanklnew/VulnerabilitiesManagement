from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.db import models
from hosts.models import HostModel
from services.models import ServiceModel
from django.contrib.auth.models import User
from projects.models import ScanProjectModel
from hosts.models import HostModel
from vulnerabilities.models import VulnerabilityModel

REPORT_STORAGE = FileSystemStorage(location=getattr(settings, 'PATH_ATTACHMENT'))


class ScanTaskModel(models.Model):
    name = models.CharField(max_length=128, verbose_name='Name of Scanning Task', unique=True)
    isProcessed = models.BooleanField(verbose_name='If this task is processed', default=True)
    description = models.CharField(verbose_name='Description of scanning task', max_length=1024, blank=True, null=True)
    startTime = models.DateTimeField(verbose_name='Start time of Scanning Task', blank=True)
    endTime = models.DateTimeField(verbose_name='Finish time of Scanning Task', blank=True)
    fileAttachment = models.FileField(verbose_name='File attachment', blank=True, null=True, storage=REPORT_STORAGE)
    submitter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submitter')
    scanBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scanBy', blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdate = models.DateTimeField(auto_now=True)
    scanProject = models.ForeignKey(to=ScanProjectModel, on_delete=models.CASCADE, related_name="ScanProjectScanTask")

    def __str__(self):
        return self.name

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.startTime > self.endTime:
            raise ValidationError('Start time cannot precede end time')


class ScanInfoModel(models.Model):
    hostScanned = models.ForeignKey(to=HostModel, on_delete=models.CASCADE, related_name="ScanInfoHost")
    vulnFound = models.ManyToManyField(VulnerabilityModel, blank=True, related_name="ScanInfoVuln")
    scanTask = models.ForeignKey(to=ScanTaskModel, on_delete=models.CASCADE, related_name="ScanInfoScanTask")

    def __str__(self):
        return self.hostScanned.hostName + ' - ' + self.hostScanned.ipAddr
