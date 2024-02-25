from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.

class Dashboard(View):
    template_name = "dashboard.html"
    def get(self, request):
        context = {}

        return render(request, self.template_name, context)