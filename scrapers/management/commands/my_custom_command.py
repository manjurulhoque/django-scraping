from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "A description of the command"

    def handle(self, *args, **options):
        pass
