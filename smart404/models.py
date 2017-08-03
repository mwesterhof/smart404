# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.sites.models import Site
from django.db import models
from django.utils.timezone import now


class NotFoundEntry(models.Model):
    site = models.ForeignKey(Site, related_name='not_found_entries', null=True)
    url = models.CharField(max_length=512)
    redirect_to = models.CharField(blank=True, max_length=512, null=True)
    permanent = models.BooleanField(default=False)

    first_seen = models.DateTimeField(default=now)
    last_seen = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.last_seen = now()
        return super(NotFoundEntry, self).save(*args, **kwargs)
