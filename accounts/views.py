from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

from . import forms

# Create your views here.
class SignUp(CreateView):
    form_class = forms.signupform
    success_url  = reverse_lazy('login')
    template_name = 'accounts/signup.html'


@login_required(redirect_field_name='test')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
