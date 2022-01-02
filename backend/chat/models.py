from django.db import models

# Create your models here.

class Dictionary(models.Model):
    GENERAL = "GENERAL"
    DEVELOPER = "DEVELOPER"
    DESK_AND_DASHBOARD = "DESK_AND_DASHBOARD"

    TAG = (
        (GENERAL, "GENERAL"),
        (DEVELOPER, "DEVELOPER"),
        (DESK_AND_DASHBOARD, "DESK_AND_DASHBOARD"),
    )

    tags = models.CharField(max_length=30, choices=TAG, default=GENERAL)
    term = models.CharField(max_length=30, null=False)
    description = models.TextField()
    full_name = models.CharField(max_length=100, null=True, blank=True)
    attached_link = models.URLField(blank=True, null=True)
    examples = models.TextField(blank=True, null=True)
    sendbird_usage = models.PositiveSmallIntegerField(null=True, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}-{self.term}]'

    def get_absolute_url(self):
        return f'/dictionary/{self.pk}/'
