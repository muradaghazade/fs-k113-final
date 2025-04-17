from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from accounts.forms import * 
from django.urls import reverse_lazy
from accounts.models import User
from django.contrib.auth.views import *

class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/accounts/login/'

class EditProfile(UpdateView):
    model = User
    template_name = 'edit_profile.html'
    form_class = EditProfileForm
    success_url = '/'
    def get_object(self):
        return self.request.user
    
    def get_sucess_url(self):
        return reverse_lazy('account:user-profile', args=(self.request.user.id))

class LoginUser(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

def user_profile(request, id):
    user = User.objects.get(id=id)
    context = {
        'user': user,
    }
    return render(request, 'user-profile.html', context)

class ChangePassword(PasswordChangeView):
    template_name = 'change_password.html'
    form_class = LoginForm
    success_url = '/'
