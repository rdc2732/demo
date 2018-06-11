# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Feature(models.Model):
    CHOICE = u'CHO'
    SELECTION = u'SEL'
    RULE_TYPES = ((CHOICE, u'choice'), (SELECTION, u'selection'))
    group = models.CharField(max_length=50, blank=True)
    function = models.CharField(max_length=50, blank=True)
    feature_name = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=50, blank=True) # keyword or feature
    rule_type = models.CharField(max_length=15, blank=True, choices=RULE_TYPES)
    option_min = models.IntegerField(blank=True, null=True)
    option_max = models.IntegerField(blank=True, null=True)
    enabled = models.NullBooleanField(default=False)
    selected = models.NullBooleanField(default=False)
    dependency = models.ManyToManyField('self', related_name='dependent', symmetrical=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
