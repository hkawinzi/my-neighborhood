from django.shortcuts import render,get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.db.models import Sum
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .forms import UpdateProfileForm, NewHoodForm,NewPostForm,NewBusinessForm
from .models import Profile,Neighbourhood,Business,Post


def home(request,id):
    current_user = request.user
    hood = Neighbourhood.objects.get(id=id)
    posts = Post.objects.filter(hood_id=id)
    businesses = Business.objects.filter(biz_hood=id)
    profile = Profile.objects.get(user=current_user)
    if request.method == 'POST':
        form = NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner=current_user
            post.profile=profile
            post.hood = hood
            post.save()
            return redirect(home,id)
    else:
        form = NewPostForm()
    return render(request,'home.html',{'hood':hood,'form':form,'posts':posts,'businesses':businesses})

@login_required(login_url='/accounts/login/')
def setup_hood(request):
    try:
        profile = Profile.objects.get(user_id=request.user.id)
    except ObjectDoesNotExist:
            return redirect('setup_profile_hood')
    current_user = request.user
    if request.method == 'POST':
        form = NewHoodForm(request.POST,request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.headman=current_user
            hood.save()
            return redirect(home,hood.id)
    else:
        form = NewHoodForm()
    return render(request,'create_hood/new_hood.html',{'form':form,'user':current_user})



