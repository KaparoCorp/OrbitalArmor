from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import View, TemplateView
from .forms import RegistrationForm
from .models import CustomUser
from django.contrib.auth import authenticate

# Create your views here.
#Home/Landing page View
class HomePage(View):
    template_name = "home.html"
    def get(self, request):
        context = {}
        return render(request, self.template_name, context)

#registration View
class Registration(View):
    template_name = "registration.html"
    context = {}

    #get request
    def get(self, request):
        context = {}   
        form = RegistrationForm()
        context = {'form': form}
        return render(request, self.template_name, context)
    
    #post request 
    def post(self, request ):
        form = RegistrationForm(request.POST or None)
        context = {'form': form}
        if form.is_valid():
            form.save()
            return redirect('/signIn/')
        return render(request, self.template_name, context)

#sign in view
class SignIn(View):
    template_name = "login.html"
    users=CustomUser.objects.all()
    
    #get request
    def get(self, request):
        context = {}
        return render(request, self.template_name, context)
    
    #post request
    def post(self, request):
        if request.method == 'POST':
            user_name = request.POST.get('username')
            password = request.POST.get('password')
            user = CustomUser.objects.get(username=user_name)
            User = authenticate(username=user_name, password=password)
            if User is not None:
                pass
            else:
                print("User Failed")
                return redirect('/signIn')
            
        return HttpResponseRedirect('/dashboard/')
    
#about us page View
class AboutUs(View):
    template_name = "about.html"

    #get request
    def get(self, request):
        context = {}
        return render(request, self.template_name, context)

#History page View
class History(View):
    template_name = "history.html"

    #get request
    def get(self, request):
        context = {}
        return render(request, self.template_name, context)
