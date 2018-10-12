from django.contrib.auth.models import User, Group, Permission
from django.db.models import Q

PERMS_APPS = ['projects', 'scans', 'vulnerabilities', 'hosts', 'services', 'submit']

# Check if superuser is exist
user = User.objects.filter(is_superuser=True)
if not user:
    User.objects.create_superuser('admin', None, 'P@ssw0rd')
    print('[+] Created superuser admin')
else:
    print('[i] Superuser is already existed')

# Group submitter
submitter, created = Group.objects.get_or_create(name='submitter')
if created:
    print('[+] Created group submitter')
else:
    print('[i] Group submitter is already existed')

perms = Permission.objects.filter(Q(content_type__app_label__in=PERMS_APPS), codename__icontains='add')
for perm in perms:
    submitter.permissions.add(perm)
submitter.save()
print('[+] Assigned permissions to group submitter')

# Group manager
manager, created = Group.objects.get_or_create(name='manager')
if created:
    print('[+] Created group manager')
else:
    print('[i] Group manager is already existed')

perms = Permission.objects.filter(content_type__app_label__in=PERMS_APPS)
for perm in perms:
    manager.permissions.add(perm)
manager.save()
print('[+] Assigned permissions to group manager')



