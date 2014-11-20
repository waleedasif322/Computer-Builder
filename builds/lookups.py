from ajax_select import LookupChannel
from django.db.models import Q
from django.utils.html import escape
from parts.models import *

class MoboLookup(object):

    model = MoboListing

    def get_query(self, q, request):
        return MoboListing.objects.filter(moboList__icontains=q)

    def get_result(self, obj):
        """ result is the simple text that
        is the completion of what the person typed """
        return obj.moboList

    #def get_price(self, obj):
     #   return obj.moboPrice

    def format_match(self, obj):
        """ (HTML) formatted item for display in the dropdown """
        return self.format_item_display(obj)

    def format_item_display(self, obj):
        """ (HTML) formatted item for 
        displaying item in the selected deck area """
        return u"%s<div><i>$%s</i></div>" % (escape(obj.moboList), escape(obj.moboPrice))

    def format_result(self,strain):
        """ This controls the display of the dropdown menu.
        This is set to show the unicode name of the strain."""
        return unicode(strain)

    def format_item(self, obj):
        """The display of a currently selected object
        in the area below the search box. html is OK """
        return unicode(obj)

    def get_objects(self, ids):
        return MoboListing.objects.filter(pk__in=ids)

class CpuLookup(object):

    model = CpuListing

    def get_query(self, q, request):
        """Finds the match in the database of CPU parts"""
        return CpuListing.objects.filter(cpuList__icontains=q)

    def get_result(self, obj):
        """ result is the simple text that
        is the completion of what the person typed """
        return obj.cpuList

    #def get_price(self, obj):
     #   return obj.cpuPrice

    def format_match(self, obj):
        """ (HTML) formatted item for display in the dropdown """
        return self.format_item_display(obj)

    def format_item_display(self, obj):
        """ (HTML) formatted item for displaying 
        item in the selected deck area """
        return u"%s<div><i>$%s</i></div>" % (escape(obj.cpuList), escape(obj.cpuPrice))

    def format_result(self,obj):
        """ This controls the display of the dropdown menu.
        This is set to show the unicode name of the cpu."""
        return unicode(obj)

    def format_item(self, obj):
        """The display of a currently selected object 
        in the area below the search box. html is OK """
        return unicode(obj)

    def get_objects(self, ids):
        return CpuListing.objects.filter(pk__in=ids)

class GpuLookup(object):

    model = GpuListing

    def get_query(self, q, request):
        """ Finds the match in the database of GPU parts """
        return GpuListing.objects.filter(gpuList__icontains=q)

    def get_result(self, obj):
        """ result is the simple text that is 
        the completion of what the person typed """
        return obj.gpuList

    #def get_price(self, obj):
     #   return obj.gpuPrice

    def format_match(self, obj):
        """ (HTML) formatted item for display in the dropdown """
        return self.format_item_display(obj)

    def format_item_display(self, obj):
        """ (HTML) formatted item for displaying 
        item in the selected deck area """
        return u"%s<div><i>$%s</i></div>" % (escape(obj.gpuList), escape(obj.gpuPrice))

    def format_result(self, obj):
        """ This controls the display of the dropdown menu.
        This is set to show the unicode name of the GPU."""
        return unicode(obj)

    def format_item(self, obj):
        """The display of a currently selected object 
        in the area below the search box. html is OK """
        return unicode(obj)

    def get_objects(self, ids):
        return GpuListing.objects.filter(pk__in=ids)

class CaseLookup(object):

    model = CaseListing

    def get_query(self, q, request):
        """Finds the match in the database of CPU parts"""
        return CaseListing.objects.filter(caseList__icontains=q)

    def get_result(self, obj):
        """ result is the simple text that is 
        the completion of what the person typed """
        return obj.caseList

    #def get_price(self, obj):
     #   return obj.casePrice

    def format_match(self, obj):
        """ (HTML) formatted item for display in the dropdown """
        return self.format_item_display(obj)

    def format_item_display(self, obj):
        """ (HTML) formatted item for displaying 
        item in the selected deck area """
        return u"%s<div><i>$%s</i></div>" % (escape(obj.caseList), escape(obj.casePrice))

    def format_result(self, obj):
        """ This controls the display of the dropdown menu.
        This is set to show the unicode name of the cpu."""
        return unicode(obj)

    def format_item(self, obj):
        """The display of a currently selected 
        object in the area below the search box. html is OK """
        return unicode(obj)

    def get_objects(self, ids):
        return CaseListing.objects.filter(pk__in=ids)

class MemLookup(object):

    model = MemListing

    def get_query(self, q, request):
        """Finds the match in the database of RAM memory parts"""
        return MemListing.objects.filter(memList__icontains=q)

    def get_result(self, obj):
        """ result is the simple text that is the 
        completion of what the person typed """
        return obj.memList

   # def get_price(self, obj):
    #    return obj.memPrice

    def format_match(self, obj):
        """ (HTML) formatted item for display in the dropdown """
        return self.format_item_display(obj)

    def format_item_display(self, obj):
        """ (HTML) formatted item for displaying 
        item in the selected deck area """
        return u"%s<div><i>$%s</i></div>" % (escape(obj.memList), escape(obj.memPrice))

    def format_result(self, obj):
        """ This controls the display of the dropdown menu.
        This is set to show the unicode name of the memory."""
        return unicode(obj)

    def format_item(self, obj):
        """The display of a currently selected object 
        in the area below the search box. html is OK """
        return unicode(obj)

    def get_objects(self, ids):
        return MemListing.objects.filter(pk__in=ids)

class HdLookup(object):

    model = HdListing

    def get_query(self, q, request):
        """Finds the match in the 
        database of Hard Drive parts"""
        return HdListing.objects.filter(hdList__icontains=q)

    def get_result(self, obj):
        """ result is the simple text that is 
        the completion of what the person typed """
        return obj.hdList

    #def get_price(self, obj):
     #   return obj.hdPrice

    def format_match(self, obj):
        """ (HTML) formatted item for display in the dropdown """
        return self.format_item_display(obj)

    def format_item_display(self, obj):
        """ (HTML) formatted item for displaying
        item in the selected deck area """
        return u"%s<div><i>$%s</i></div>" % (escape(obj.hdList), escape(obj.hdPrice))

    def format_result(self, obj):
        """ This controls the display of the dropdown menu. 
        This is set to show the unicode name of the hard drive."""
        return unicode(obj)

    def format_item(self, obj):
        """The display of a currently selected
        object in the area below the search box. html is OK """
        return unicode(obj)

    def get_objects(self, ids):
        return HdListing.objects.filter(pk__in=ids)
