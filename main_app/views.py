from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from .models import Team
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse


# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"
    
class About(TemplateView):
    template_name = "about.html"
    
class TeamList(TemplateView):
    template_name = "team_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["teams"] = Team.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["teams"] = Team.objects.all() # this is where we add the key into our context object for the view to use
            context["header"] = "Teams"
        return context
    
class TeamCreate(CreateView):
    model = Team
    fields = ['name', 'img', 'bio']
    template_name = "team_create.html"
    def get_success_url(self):
        return reverse('team_detail', kwargs={'pk': self.object.pk})
    
class TeamDetail(DetailView):
    model = Team
    template_name = "team_detail.html"
    
class TeamUpdate(UpdateView):
    model = Team
    fields = ['name', 'img', 'bio']
    template_name = "team_update.html"
    def get_success_url(self):
        return reverse('team_detail', kwargs={'pk': self.object.pk})
    
class TeamDelete(DeleteView):
    model = Team
    template_name = "team_delete_confirmation.html"
    success_url = "/teams/"
