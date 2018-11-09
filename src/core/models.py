# This file contains the helper models
# and also the core models which are not
# part of any of the apps or api

from django.db import models


class TimestampedModel(models.Model):
    # A timestamp representing when this object was created.
    created_at = models.DateTimeField(auto_now_add=True)

    # A timestamp representing when this object was last updated.
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

        # reverse order
        ordering = ['-created_at', '-updated_at']
