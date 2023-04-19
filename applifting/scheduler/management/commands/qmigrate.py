from django.core.management.base import BaseCommand
from applifting.scheduler.scheduler import schedule_tasks


class Command(BaseCommand):
    """Django command to migrate schedules"""

    def handle(self, *args, **options):
        schedule_tasks()
