from django.core.management.base import BaseCommand, CommandError

# https://medium.com/analytics-vidhya/writing-custom-management-commands-in-django-d66044c37433


class Command(BaseCommand):
    help = "The command of the year"

    def handle(self, *args, **options):
        try:
            print("Command is ok !")
        except Exception as e:
            raise CommandError(e)
