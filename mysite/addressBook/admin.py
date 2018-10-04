# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
# adds model to admin dashboard
from .models import Person
admin.site.register(Person)
