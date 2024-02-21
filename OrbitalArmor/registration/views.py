from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.

class HomePage(View):
    template_name = "home.html"
    def get(self, request):
        context = {

        }
        return render(request, self.template_name, context)
    
class AboutView(TemplateView):
    template_name = "about.html"

class Historty(TemplateView):
    template_name = "history.html"

class SignIn(View):
    template_name = "signin.html"
    def get(self, request):
        context = {}
        return render(request, self.template_name, context)