from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from .forms import RegistrationForm
from .models import CustomUser

# Create your views here.

class HomePage(View):
    template_name = "home.html"
    def get(self, request):
        context = {}
        return render(request, self.template_name, context)
    
class AboutView(TemplateView):
    template_name = "about.html"

class Historty(TemplateView):
    template_name = "history.html"


class SignIn(View):
    template_name = "login.html"
    def get(self, request):
        context = {}
        return render(request, self.template_name, context)
    
class Registration(View):
    template_name = "registration.html"
    context = {}

    def get(self, request):
        context = {}   
        form = RegistrationForm()
        context = {'form': form}
        return render(request, self.template_name, context)
    
    def post(self, request ):
        form = RegistrationForm(request.POST or None)
        context = {'form': form}
        if form.is_valid():
            form.save()
            
            return redirect('/signIn/')
        return render(request, self.template_name, context)
