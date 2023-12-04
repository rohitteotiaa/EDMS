# assignments/management/commands/create_duties.py

from django.core.management.base import BaseCommand
from app.models import zone

class Command(BaseCommand):
    help = 'Creates Zone objects with names "Manager" and "Team Leader"'

    def handle(self, *args, **kwargs):
        zone.objects.get_or_create(name="A")
        zone.objects.get_or_create(name="B")
        zone.objects.get_or_create(name="C")
        zone.objects.get_or_create(name="D")
        zone.objects.get_or_create(name="E")
        zone.objects.get_or_create(name="F")
        zone.objects.get_or_create(name="G")
        zone.objects.get_or_create(name="H")
        zone.objects.get_or_create(name="I")
        zone.objects.get_or_create(name="J")
        zone.objects.get_or_create(name="K")
        zone.objects.get_or_create(name="L")
        zone.objects.get_or_create(name="M")
        zone.objects.get_or_create(name="N")
        zone.objects.get_or_create(name="O")
        zone.objects.get_or_create(name="P")
        zone.objects.get_or_create(name="Q")
        zone.objects.get_or_create(name="R")
        zone.objects.get_or_create(name="S")
        zone.objects.get_or_create(name="T")
        zone.objects.get_or_create(name="U")
        zone.objects.get_or_create(name="V")
        zone.objects.get_or_create(name="W")
        zone.objects.get_or_create(name="X")
        zone.objects.get_or_create(name="Y")
        zone.objects.get_or_create(name="Z")
        

        



