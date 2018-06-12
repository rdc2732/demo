# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from fmm.models import Feature

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

# Create your views here.
def index(request):
    return HttpResponse(u"You're looking at the demo/fmm home page.")

class FeatureList(ListView):
    queryset = Feature.objects.prefetch_related().all()


def loadfmm(request):
    fmm = open(u'FMM.txt', u'r')
    dependency_list = []

    line_count = 0
    print "lfmm: ", Feature.objects.count()
    if Feature.objects.count() > 0:
        Feature.objects.all().delete()
    print "lfmm: ", Feature.objects.count()
    for line in fmm:
        # 0-Group, 1-Function, 2-Feature_Name, 3-Feature, 4-Dependency, 5-Rule, 6-Min, 7-Max

        # CHOICE = u'CHO'
        # SELECTION = u'SEL'
        # RULE_TYPES = ((CHOICE, u'choice'), (SELECTION, u'selection'))
        # group = models.CharField(max_length=50, blank=True)
        # function = models.CharField(max_length=50, blank=True)
        # feature_name = models.CharField(max_length=100, blank=True)
        # name = models.CharField(max_length=50, blank=True)  # keyword or feature
        # rule_type = models.CharField(max_length=15, blank=True, choices=RULE_TYPES)
        # option_min = models.IntegerField(blank=True, null=True)
        # option_max = models.IntegerField(blank=True, null=True)
        # enabled = models.NullBooleanField(default=False)
        # selected = models.NullBooleanField(default=False)
        # dependency = models.ManyToManyField('self', related_name='dependent', symmetrical=False)
        # completed = models.BooleanField(default=False)

        line_data = line.rstrip().split(u',')
        group_name = line_data[0]
        function_name = line_data[1]
        feature_name = line_data[2]
        feature = line_data[3] # 'name' in the model
        dependencies = line_data[4].split(u';')
        rule_type = line_data[5]
        option_min = line_data[6]
        option_max = line_data[7]

        f = Feature(
            group=group_name,
            function=function_name,
            feature_name=feature_name,
            name=feature,
            rule_type=rule_type,
            option_min=option_min,
            option_max=option_max,
            completed=True
          )
        f.save()

        for  dependency in dependencies:
            dependency_list.append((feature,dependency))

        line_count += 1
        print "lines processed:", line_count

    for item in dependency_list:
        f = Feature.objects.filter(name=item[0]).first()
        d = Feature.objects.filter(name=item[1]).first()
        if f and d:
            f.dependency.add(d)
        else:
            if f:
                print 'd = ', item[1]
            else:
                print 'f = ', item[0]


    response_text = u'FMM.txt load complete. ' + str(line_count) + u' records Processed. '
    return HttpResponse(response_text)
