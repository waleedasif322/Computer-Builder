from django.contrib import admin
from builds.models import BuildsTable
from parts.models import *
from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin

class MobosAdmin(AjaxSelectAdmin):
    """
    # create an ajax form class using the factory function
    #
    # model,fieldlist,   [form superclass]
    """

    form = make_ajax_form(MoboListing, {'moboList':'moboListing'})

class CpusAdmin(AjaxSelectAdmin):
    """
    # create an ajax form class using the factory function
    # model,fieldlist,   [form superclass]
    """
 
    form = make_ajax_form(CpuListing, {'cpuList':'cpuListing'})

class GpusAdmin(AjaxSelectAdmin):
    """
    # create an ajax form class using the factory function
    # model,fieldlist,   [form superclass]
    """

    form = make_ajax_form(GpuListing, {'gpuList':'gpuListing'})


class CasesAdmin(AjaxSelectAdmin):
    """
    # create an ajax form class using the factory function
    # model,fieldlist,   [form superclass]
    """

    form = make_ajax_form(CaseListing, {'caseList':'caseListing'})

class HdAdmin(AjaxSelectAdmin):
    """
    # create an ajax form class using the factory function
    # model,fieldlist,   [form superclass]
    """

    form = make_ajax_form(HdListing, {'hdList':'hdListing'})

class MemAdmin(AjaxSelectAdmin):
    """
    # create an ajax form class using the factory function
    # model,fieldlist,   [form superclass]
    """

    form = make_ajax_form(MemListing, {'memList':'memListing'})

admin.site.register(GpuListing, GpusAdmin)
admin.site.register(BuildsTable)
admin.site.register(CpuListing, CpusAdmin)
admin.site.register(CaseListing, CasesAdmin)
admin.site.register(HdListing, HdAdmin)
admin.site.register(MoboListing, MobosAdmin)
admin.site.register(MemListing, MemAdmin)
