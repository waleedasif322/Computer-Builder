""" 
The fields in this module have been 
created for the autocomplete functionality 
"""

from django.forms.models import ModelForm
from django import forms
from ajax_select import make_ajax_field
from parts.models import *
from builds.models import BuildsTable

class MoboForm(ModelForm):
    """
    The autocompletefield for 
    motherboards
    """
    moboList = make_ajax_field(MoboListing, 'moboList', 'moboList', help_text=None)
    class Meta:
        """
        Here we are linking field and model
        """
        model = MoboListing

    

class CpuForm(ModelForm):
    """
    The autocompletefield for motherboards
    """
    cpuList = make_ajax_field(CpuListing, 'cpuList', 'cpuList', help_text=None)
    class Meta:
        """
        Here we are linking field and model
        """
        model = CpuListing

    

class CaseForm(ModelForm):
    """
    The autocompletefield for motherboards
    """
    caseList = make_ajax_field(CaseListing, 'caseList', 'caseList', help_text=None)
    class Meta:
        """
        Here we are linking field and model
        """
        model = CaseListing

    

class MemForm(ModelForm):
    """
    The autocompletefield for motherboards
    """
    memList = make_ajax_field(MemListing, 'memList', 'memList', help_text=None)
    class Meta:
        """
        Here we are linking field and model
        """
        model = MemListing

    

class GpuForm(ModelForm):
    """
    The autocompletefield for motherboards
    """
    gpuList = make_ajax_field(GpuListing, 'gpuList', 'gpuList', help_text=None)
    class Meta:
        """
        Here we are linking field and model
        """
        model = GpuListing

    

class HdForm(ModelForm):
    """
    The autocompletefield for motherboards
    """
    hdList = make_ajax_field(HdListing, 'hdList', 'hdList', help_text=None)
    class Meta:
        """
        Here we are linking field and model
        """
        model = HdListing

    
