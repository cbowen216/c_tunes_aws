from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import BadHeaderError
from django.template import loader
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# Create your views here.
User = get_user_model()

def userlist(request):
    context = {
        'users': User.objects.all()
    }
    return render(request,'users/list.html', context)

def register(request):
    next = request.GET.get('next', '/')
    try:
        username = request.POST['username']
        password = request.POST['password']
        auth_user = authenticate(request, username=username, password=password)
        try:
            login(request, auth_user)
            return HttpResponseRedirect(next)
        except:
            messages.error(request, 'Invalid credentials')
            return HttpResponseRedirect(next)
    except (KeyError):
        messages.error(request, 'Invalid credentials')
        #return render(request, '/', { 'message': "Invalid username or password. Please try again." })


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,
                            f'{username} Your account has been created! You can now login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

@login_required
def userhome(request):
    return render(request, 'users/home.html')