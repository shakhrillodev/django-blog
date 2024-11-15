from django.shortcuts import render
from django.contrib.auth import logout
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

def user_logout(request):
    logout (request)
    return render (request, 'registration/logged_out.html')

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'