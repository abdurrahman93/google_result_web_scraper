from django.db import models

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class GoogleResult(TimeStamp):
    query_param = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    url = models.TextField(blank=True)
