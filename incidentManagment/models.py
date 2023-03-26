from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import random
from django.contrib.auth.models import AbstractUser

class Incident(models.Model):
    INCIDENT_STATUS_OPEN = 'Open'
    INCIDENT_STATUS_IN_PROGRESS = 'In progress'
    INCIDENT_STATUS_CLOSED = 'Closed'
    INCIDENT_STATUS_CHOICES = [
        (INCIDENT_STATUS_OPEN, 'Open'),
        (INCIDENT_STATUS_IN_PROGRESS, 'In progress'),
        (INCIDENT_STATUS_CLOSED, 'Closed'),
    ]

    INCIDENT_PRIORITY_HIGH = 'High'
    INCIDENT_PRIORITY_MEDIUM = 'Medium'
    INCIDENT_PRIORITY_LOW = 'Low'
    INCIDENT_PRIORITY_CHOICES = [
        (INCIDENT_PRIORITY_HIGH, 'High'),
        (INCIDENT_PRIORITY_MEDIUM, 'Medium'),
        (INCIDENT_PRIORITY_LOW, 'Low'),
    ]

    incident_id = models.CharField(max_length=13, unique=True, editable=False)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    incident_details = models.TextField()
    reported_date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=10, choices=INCIDENT_PRIORITY_CHOICES)
    status = models.CharField(max_length=20, choices=INCIDENT_STATUS_CHOICES)

    def save(self, *args, **kwargs):
        if not self.incident_id:
            # generate unique incident ID
            year = datetime.now().year
            random_number = random.randint(10000, 99999)
            self.incident_id = f'RMG{random_number}{year}'

        super(Incident, self).save(*args, **kwargs)

    def __str__(self):
        return self.incident_id
