from django.shortcuts import render,redirect
from .models import Conference
from django.views.generic import ListView , DetailView , CreateView , UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ConferenceForm

# Vue fonctionnelle pour la liste
def liste_conferences(request):
    conferences_list = Conference.objects.all()
    return render(request, "conferences/liste.html", {"liste": conferences_list})

def details_index(request):
    return redirect("liste_conferences")

class ConferenceList(ListView):
    model=Conference
    context_object_name="liste"
    template_name="conferences/liste.html"
    
class ConferenceDetails(DetailView):
    model = Conference
    template_name = "conferences/details.html"
    context_object_name = "conference"

class ConferenceCreate(CreateView):
    model = Conference
    template_name = "conferences/form.html"
    #fields = ["name", "theme", "location", "description", "start_date", "end_date"]
    form_class=ConferenceForm
    success_url = reverse_lazy("liste_conferences")

class ConferenceUpdate(UpdateView):
    model = Conference
    template_name = "conferences/form.html"
    #fields = ["name", "theme", "location", "description", "start_date", "end_date"]
    form_class=ConferenceForm
    success_url = reverse_lazy("liste_conferences")

class ConferenceDelete(DeleteView):
    model = Conference
    template_name = "conferences/delete.html"
    success_url = reverse_lazy("liste_conferences")