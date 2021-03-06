from django.shortcuts import render
from TheApp.forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, TemplateView, ListView, DetailView
from. import models
# Create your views here.
def index(request):
    return render(request, 'TheApp/index.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('TheApp:index'))


def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'TheApp/registration.html', {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('TheApp:index'))

            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse('invalid login details supplied')
    else:
        return render(request, 'TheApp/login.html',)


def userblog(request):
    return render(request, 'TheApp/userblog.html')

def draft(request):
    if request.method == 'POST':
        draft = request.POST.get('post_content')
        return render(request, 'TheApp/draft.html', {'draft':draft})
#רציתי להכניס לdraft את הערך של הpost_content שזה השם שנתתי לtextarea אבל זה לא עבד.
#לא מחקתי את שורת הקוד כי עדיין לא פתרתי את הבעיה (למרות שבדף של הdraft.html אני מנסה דרך אחרת בעזרת js)

    else:
        return render(request, 'TheApp/userblog.html',)


class Explore(ListView):
    context_object_name = 'blogs'
    model = models.UserProfileInfo
    template_name = 'TheApp/explore.html'
