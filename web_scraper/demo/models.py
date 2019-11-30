from django.db import models


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, help_text='Record created at.')
    updated_at = models.DateTimeField(auto_now=True, help_text='Record updated at.')

    class Meta:
        abstract = True


class GoogleResult(TimeStamp):
    query_param = models.CharField(max_length=200, help_text='Text to be queried in search engine.')
    text = models.TextField(blank=True, help_text='Text for particular returned result.')
    url = models.TextField(blank=True, help_text='Url for particular returned result.')
