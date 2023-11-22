from django.core.management.base import BaseCommand, CommandError
from django.core.mail import EmailMessage
from my_app.models import Report

# https://medium.com/analytics-vidhya/writing-custom-management-commands-in-django-d66044c37433


class Command(BaseCommand):
    help = "Send all unsent reports"

    def handle(self, *args, **options):
        try:
            reports = Report.objects.filter(sent=False)
            if reports.exists():
                for report in reports:
                    subject = "Report"
                    receiver = report.receiver
                    content = report.content
                    new_email = EmailMessage(
                        subject, content, 'gabrieltrouve5@gmail.com', [receiver]
                    )
                    new_email.send()
                    report.sent = True
                    report.save()

        except Exception as e:
            raise CommandError(e)
