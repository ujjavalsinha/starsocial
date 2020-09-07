from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from accounts.forms import UserCreateForm
# Create your views here.

class SignUp(CreateView):
    form_class = UserCreateForm
    model = User
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
