# assignments/management/commands/create_duties.py

from django.core.management.base import BaseCommand
from app.models import room_number

class Command(BaseCommand):
    help = 'Creates room_number objects with names "Manager" and "Team Leader"'

    def handle(self, *args, **kwargs):
        room_number.objects.get_or_create(name="101")
        room_number.objects.get_or_create(name="102")
        room_number.objects.get_or_create(name="103")
        room_number.objects.get_or_create(name="104")
        room_number.objects.get_or_create(name="105")
        room_number.objects.get_or_create(name="106")
        room_number.objects.get_or_create(name="107")
        room_number.objects.get_or_create(name="108")
        room_number.objects.get_or_create(name="109")
        room_number.objects.get_or_create(name="110")
        room_number.objects.get_or_create(name="111")
        room_number.objects.get_or_create(name="112")
        room_number.objects.get_or_create(name="113")
        room_number.objects.get_or_create(name="114")
        room_number.objects.get_or_create(name="115")
        room_number.objects.get_or_create(name="201")
        room_number.objects.get_or_create(name="202")
        room_number.objects.get_or_create(name="203")
        room_number.objects.get_or_create(name="204")
        room_number.objects.get_or_create(name="205")
        room_number.objects.get_or_create(name="206")
        room_number.objects.get_or_create(name="207")
        room_number.objects.get_or_create(name="208")
        room_number.objects.get_or_create(name="209")
        room_number.objects.get_or_create(name="210")
        room_number.objects.get_or_create(name="211")
        room_number.objects.get_or_create(name="212")
