from django.db import models


SEVERITY_CHOICES = [
    ("info", "Informational"),
    ("warning", "Warning"),
    ("error", "Error"),
]

class Alert(models.Model):
    agent = models.ForeignKey(
        "agents.Agent",
        related_name="agent",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    message = models.TextField(null=True, blank=True)
    alert_time = models.DateTimeField(null=True, blank=True)
    snooze_until = models.DateTimeField(null=True, blank=True)
    resolved = models.BooleanField(default=False)
    severity = models.CharField(
        max_length=100, choices=SEVERITY_CHOICES, default="info"
    )

    def __str__(self):
        return self.message