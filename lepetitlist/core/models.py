from django.db import models
from django.utils import timezone

class Lists(models.Model):
    list_name = models.CharField(max_length=255, default='to do', null=False)
    list_description = models.TextField(max_length=1000, null=True)
    list_date = models.DateField(default=timezone.now, blank=True)
    list_time = models.TimeField(default=timezone.now().time, blank=True)
    

    class Meta:
        verbose_name_plural = 'Lists'

    def __str__(self) -> str:
        return self.list_name

