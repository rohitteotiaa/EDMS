# assignments/management/commands/create_duties.py

from django.core.management.base import BaseCommand
from app.models import section

class Command(BaseCommand):
    help = 'Creates section objects with names "Manager" and "Team Leader"'

    def handle(self, *args, **kwargs):
        section.objects.get_or_create(name="1")
        section.objects.get_or_create(name="2")
        section.objects.get_or_create(name="3")
        section.objects.get_or_create(name="4")
        section.objects.get_or_create(name="5")
        section.objects.get_or_create(name="6")
        section.objects.get_or_create(name="7")
        section.objects.get_or_create(name="8")
        section.objects.get_or_create(name="9")
        section.objects.get_or_create(name="10")
        section.objects.get_or_create(name="11")
        section.objects.get_or_create(name="12")
        section.objects.get_or_create(name="13")
        section.objects.get_or_create(name="14")
        section.objects.get_or_create(name="15")
        section.objects.get_or_create(name="16")
