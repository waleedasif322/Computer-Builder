"""
We just load the Cover Page
"""
from django.shortcuts import render

def cover_page(request):
    """
    Load the cover PAge
    """
    return render(request, "cover_page.html", {'title_name':'Computer Builder'})

def about_page(request):
    """
    Load the about PAge
    """
    return render(request, "about_page.html", {'title_name':'Computer Builder'})

def contact_page(request):
    """
    Load the contact PAge
    """
    return render(request, "contact_page.html", {'title_name':'Computer Builder'})



