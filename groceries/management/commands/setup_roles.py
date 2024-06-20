from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from groceries.models import Item

class Command(BaseCommand):
    help = 'Set up user roles and permissions'

    def handle(self, *args, **kwargs):
        # Create dbadmin group
        dbadmin, created = Group.objects.get_or_create(name='dbadmin')
        if created:
            self.stdout.write(self.style.SUCCESS('Created dbadmin group'))
        
        # Create manager group
        manager, created = Group.objects.get_or_create(name='manager')
        if created:
            self.stdout.write(self.style.SUCCESS('Created manager group'))
        
        # Create employee group
        employee, created = Group.objects.get_or_create(name='employee')
        if created:
            self.stdout.write(self.style.SUCCESS('Created employee group'))
        
        # Define permissions for dbadmin
        dbadmin_permissions = Permission.objects.filter(content_type__app_label='groceries')
        dbadmin.permissions.set(dbadmin_permissions)

        # Define permissions for manager (customize as per your needs)
        manager_permissions = Permission.objects.filter(content_type__app_label='groceries').exclude(codename='delete_item')
        manager.permissions.set(manager_permissions)

        # Define permissions for employee (customize as per your needs)
        employee_permissions = Permission.objects.filter(content_type__app_label='groceries', codename__in=['view_item'])
        employee.permissions.set(employee_permissions)

        self.stdout.write(self.style.SUCCESS('Roles and permissions have been set up'))
