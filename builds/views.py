"""
This is the meat of the project where 
everything happens from autocomplete
to creating build and editing thems
"""
from django.shortcuts import render, render_to_response
from django import forms
import datetime
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from ajax_select.fields import AutoCompleteField
from forms import *
from builds.models import BuildsTable
from parts.models import MoboListing, CpuListing, GpuListing, HdListing, CaseListing, MemListing
from haystack.query import SearchQuerySet


class SearchForm(forms.Form):
    """ AutoCOmplete search Form """
    moboField = AutoCompleteField(
            'MoboListing',
            required=True,
            #help_text="Autocomplete will suggest motherboards",
            label="Motherboard:",
            attrs={'size': 100}
            )

    cpuField = AutoCompleteField(
            'CpuListing',
            required=True,
            #help_text="Autocomplete will suggest motherboards",
            label="Processor:",
            attrs={'size': 100}
            )

    gpuField = AutoCompleteField(
            'GpuListing',
            required=True,
            #help_text="Autocomplete will suggest motherboards",
            label="Graphics Card:",
            attrs={'size': 100}
            )

    caseField = AutoCompleteField(
            'CaseListing',
            required=True,
            #help_text="Autocomplete will suggest motherboards",
            label="Case:",
            attrs={'size': 100}
            )

    memField = AutoCompleteField(
            'MemListing',
            required=True,
            #help_text="Autocomplete will suggest motherboards",
            label="RAM Memory",
            attrs={'size': 100}
            )

    hdField = AutoCompleteField(
            'HdListing',
            required=True,
            #help_text="Autocomplete will suggest motherboards",
            label="Hard Drive",
            attrs={'size': 100}
            )

@login_required
def new_build(request):
    dico = {}
    if 'q' in request.GET:
        dico['entered'] = request.GET.get('q')
    initial = {'q': "Enter Motherboard query"}
    form = SearchForm(initial=initial)
    dico['form'] = form
    return render_to_response('new_build.html', dico,
                              context_instance=RequestContext(request))

@login_required
def create_build(request):
    """
    This is the function that stores a user build
    """
    if request.method == 'POST':

        """If an user is trying to edit the 
        build we are going to use this try except"""
        try:
            oldbuild = BuildsTable.objects.get(name=request.POST['name_input']) 

        except BuildsTable.DoesNotExist:
            new_build = True
            pass
       
        else:
            new_build = False
            oldbuild.delete()
    
        """We start by getting all the user 
        entries and storing them into variables"""
        bname = request.POST['name_input']
        mobo = request.POST['moboField']
        cpu = request.POST['cpuField']
        case = request.POST['caseField']
        mem = request.POST['memField']
        hdd = request.POST['hdField']
        gpu = request.POST['gpuField']
        acc_r = request.POST['access_right']
        username = request.user
        moboprice = MoboListing.objects.get(moboList=mobo).moboPrice
        cpuprice = CpuListing.objects.get(cpuList=cpu).cpuPrice
        caseprice = CaseListing.objects.get(caseList=case).casePrice
        memprice = MemListing.objects.get(memList=mem).memPrice
        hdprice = HdListing.objects.get(hdList=hdd).hdPrice
        gpuprice = GpuListing.objects.get(gpuList=gpu).gpuPrice  
        buildprice = moboprice + cpuprice + caseprice  
        buildprice += memprice + hdprice + gpuprice   
  
        """Now we create an instance of 
        BuildsTable and saves it to our database"""
        build = BuildsTable(name=bname, moboPart=mobo, cpuPart=cpu, 
                            casePart=case, memPart=mem, hdPart=hdd, 
                            gpuListing=gpu, user=username,
                            access_r=acc_r, price=buildprice)
        build.save()
    
    else:
        """the user got to this page somehow,
        we tell them there is an error""" 
        return render(request, 'build_error.html')  


    build_name = request.POST['name_input']
    return render(request, 'build_confirmation.html',
                  {'build_name': build_name, 'new_build': new_build})


@login_required
def edit_build(request, build_name):
    bname = build_name.replace('__', ' ')
    try:
        build = BuildsTable.objects.get(name=bname)
    except BuildsTable.DoesNotExist:
        return render(request, 'build_notexist.html', 
                      {'build_name': build_name})
    else:
        bname = build.name
        mobo = build.moboPart
        cpu = build.cpuPart
        case = build.casePart
        hdd = build.hdPart
        gpu = build.gpuListing
        mem = build.memPart
        ac_r = build.access_r        
        
        if(ac_r == 'pri'):
            private = True
        else:
            private = False

        context = {'build_name': bname, 'mobo': mobo, 'cpu': cpu, 'case': case,
                   'mem': mem, 'hdd': hdd, 'gpu': gpu, 'private': private}
        return render(request, 'build_edit.html', context)


@login_required
def show_build(request, build_name):
    #We start by getting the build from the database
    bname = build_name.replace('__', ' ')
    try:
        build = BuildsTable.objects.get(name=bname)
    except BuildsTable.DoesNotExist:
        error = True
        return render(request, 'build_error.html', {'error': berror})

    else:
        return render(request, 'build_page.html', {'abuild': build})


@login_required
def show_mybuilds(request):
    """We start by getting from the database 
    the user's builds which we order by time"""
    builds = BuildsTable.objects.filter(user=request.user).order_by('time')
    return render(request, 'build_mybuilds.html', {'builds': builds})


@login_required
def show_pubbuilds(request):
    """We start by getting from the database
    the public builds which we order by time"""
    builds = BuildsTable.objects.filter(access_r='pub').order_by('-time')
    return render(request, 'build_public.html', {'builds': builds})

@login_required
def home_page(request):
    """We start by getting from the database
    the public builds which we order by time"""
    builds = BuildsTable.objects.filter(access_r='pub').order_by('-time')
    return render(request, 'home_page.html', {'builds': builds})


@login_required
def edit_list(request):
    """Load the builds"""
    builds = BuildsTable.objects.filter(user=request.user).order_by('-time')
    return render(request, 'build_edit_list.html', {'builds': builds})

@login_required
def delete(request, build_name):
    """load the builds"""
    bname = build_name.replace('__', ' ')
    try:
        build = BuildsTable.objects.filter(user=request.user).get(name=bname)
    except BuildsTable.DoesNotExist:
        error = True
        return render(request, 'build_delete.html', {'error':error})
    else:
        build.delete()
        error = False
        return render(request, 'build_delete.html', 
                      {'error':error, 'bname':bname})
 
"""
Search Enginge coding :::::::::::::::::::::::::::::::::::::::::::::::::::
"""
@login_required
def search(request):
    """ Search page with and
    without items"""
    if request.method == 'POST':
        builds = SearchQuerySet().autocomplete(content_auto=request.POST.get(
                                               'search_text', ''))
        mode = 1 
    else:
        builds = []
        mode = 0

    return render(request, 'search.html', {'builds':builds, 'mode':mode})



