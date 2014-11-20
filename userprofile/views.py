"""
Views module for userprofiles
we just use update profile 
for creating and updating the profile
"""
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from forms import UserProfileForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

@login_required
def update_profile(request): 
    """
    This function takes care of showing
    the user profile form and saving it when changes occur
    """
    if request.method=='POST':       
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/builds/home')
    else:
        user = request.user
        profile = user.profile
        form = UserProfileForm(instance = profile)

    args = {}
    args.update(csrf(request))
    args['form'] = form
    
    return render_to_response('myprofile.html', args)
