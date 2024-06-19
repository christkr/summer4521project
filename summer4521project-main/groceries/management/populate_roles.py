from django.core.management.base import BaseCommand
from groceries.models import Role

class Command(BaseCommand):
    help = 'Populate database with initial roles'

    def handle(self, *args, **options):
        roles = ['db_admin', 'manager', 'employee']
        for role in roles:
            Role.objects.get_or_create(name=role)
        self.stdout.write(self.style.SUCCESS('Roles created successfully'))
