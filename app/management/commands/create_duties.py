# assignments/management/commands/create_duties.py

from django.core.management.base import BaseCommand
from app.models import Duty

class Command(BaseCommand):
    help = 'Creates Duty objects with names "Manager" and "Team Leader"'

    def handle(self, *args, **kwargs):
        Duty.objects.get_or_create(name="Manager")
        Duty.objects.get_or_create(name="Team Leader")
        Duty.objects.get_or_create(name="Clerk")
