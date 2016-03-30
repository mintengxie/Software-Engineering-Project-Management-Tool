from django import forms
import requirements.models.user_manager
from requirements.models import user_manager
from django.http import HttpResponse, HttpResponseRedirect
from forms import SignUpForm, ChangePwdForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.shortcuts import render, render_to_response, redirect
from django.core.mail import send_mail

# def create_user(request):
# 	if userManager.createUser(request) :
# 		return HttpResponse("Your request has been submitted. It will need to be approved by an administrator.")
# 	else:
# 		#TODO refactor to use @user_passes_test
# 		return HttpResponse("Failed to create user")


# def members(request):
#     return render(request, 'Members.html')

# def registration(request):
#     if request.method =='POST':
#         form =  RegistrationForm(request.POST)
#         if form.is_valid():
#             user_manager.createUser(request)
#             return HttpResponseRedirect('/thankYou/')
#     else:
#         form =  RegistrationForm()
#     return render(request, 'registration.html', {'form': form})

# def thank_you(request):
#     return render(request, 'ThankYou.html')

def signin(request):
    logout(request)
    username = password = ''
    errormsg = ""
    next = ""

    if request.GET:
        next = request.GET['next']
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        next = request.POST['next']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if next == '':
                    return HttpResponseRedirect('/req/projects')
                else:
                    return HttpResponseRedirect(next)
        else:
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip1 = x_forwarded_for.split(',')[-1].strip()
            else:
                ip1 = request.META.get("REMOTE_ADDR")
            errormsg0 = 'Username or Password is incorrect ! Please try again !'
            errormsg1 = ' If you fail more than 3 times, your IP address : '+str(ip1)+ " need to wait 60s for next try!"
            errormsg = errormsg0 + errormsg1
    return render_to_response('SignIn.html',
                              {'errorMsg': errormsg,
                               'next': next,
                               'isUserSigningInUpOrOut': 'true'},
                              context_instance=RequestContext(request))


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            cd = form.cleaned_data
            return render(
                request, 'SignUpFinish.html', {'form': form, 'isUserSigningInUpOrOut': 'true'})
    else:
        form = SignUpForm()
    return render(
        request, 'SignUp.html', {'form': form, 'isUserSigningInUpOrOut': 'true'})


@login_required
def signout(request):
    logout(request)
    context = {'isUserSigningInUpOrOut': 'true'}
    return render(request, 'SignOut.html', context)

# this changed by zhi and Nora
@login_required(login_url='/signin')
def changepasswd(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePwdForm(request.POST, user=user)
        if form.is_valid():
            form.save(commit=True)
            send_mail('Your password has been changed',
                      'Your password has been chenged by user: '+request.user.username,
                      'zhidou@hotmail.com', [user.email])
            logout(request)
            return HttpResponse('')
    else:
        form = ChangePwdForm(user=user)

    context = {
        'form': form,
        'title': 'Change Password',
        'confirm_message': 'After confirming changes. System will automatically logout !',
        'action': '/req/changepasswd',
        'button_desc': 'Confirm Change & Logout',
    }
    return render(request, 'ChangePasswd.html', context)


@login_required(login_url='/signin')
def userprofile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse('')
    else:
        form = UserProfileForm(instance=user)

    context = {
        'form': form,
        'title': 'Change User Profile',
        'action': '/req/userprofile',
        'button_desc': 'Change Profile'
    }
    return render(request, 'UserProfile.html', context)
