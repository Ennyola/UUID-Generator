import uuid
from django.db import models

# Create your models here.


class UUID(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    time_stamp = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-time_stamp']
