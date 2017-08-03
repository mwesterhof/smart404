# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import NotFoundEntry


class NotFoundEntryAdmin(admin.ModelAdmin):
    list_display = ['url', 'redirect_to', 'permanent', 'site']
    list_filter = ['site', 'permanent']
    list_editable = ['redirect_to', 'permanent']


admin.site.register(NotFoundEntry, NotFoundEntryAdmin)
