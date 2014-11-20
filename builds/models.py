"""
This module defines all the database model for
user builds
"""
from django.db import models
from django.contrib.auth.models import User

class BuildsTable(models.Model):

    """ 
    This is the BuildsTable model where we 
    will store everyusers different selected parts
    """

    #Access Rights defines the values that 
    #the user can enter for privacy choices
    ACCESS_RIGHTS = (('pri', 'private'),
                     ('pub', 'public'),)
    moboPart = models.CharField(max_length=400)
    cpuPart = models.CharField(max_length=200)
    casePart = models.CharField(max_length=200)
    memPart = models.CharField(max_length=200)
    hdPart = models.CharField(max_length=200)
    gpuListing = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    time = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    access_r = models.CharField(max_length=3, choices=ACCESS_RIGHTS)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    def __str__(self):
        return "%s" % self.moboPart

    def __unicode__(self):
        return "%s" % self.name 
