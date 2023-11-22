from django.db import models


class Report(models.Model):
    receiver = models.EmailField()
    content = models.TextField()
    sent = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)
