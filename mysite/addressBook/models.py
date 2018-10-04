# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# helps store phone number
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

# Create your models here.
# contact model
class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=250)
    # insatlled package to get phone number field
    phone = PhoneNumberField()
    address = models.CharField(max_length=40)
    # save person info according to time zone
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        # concatenate first and last name
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    # string representation of an object
    def __str__(self):
        return self.full_name()