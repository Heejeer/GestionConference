from django.shortcuts import render
from .models import Conference
from django.views.generic import ListView , DetailView , CreateView , UpdateView, DeleteView
from django.urls import reverse_lazy


# Vue fonctionnelle pour la liste
def liste_conferences(request):
    conferences = Conference.objects.all()
    return render(request, "conferences/liste.html", {"liste": conferences})


# Vue pour le cas où l’utilisateur tape “details/” sans pk
def details_index(request):
    return redirect("liste_conferences")


# Vue CBV pour les détails
class ConferenceDetails(DetailView):
    model = Conference
    template_name = "conferences/details.html"
    context_object_name = "conference"


# Vue CBV pour le formulaire d’ajout
class ConferenceCreate(CreateView):
    model = Conference
    template_name = "conferences/form.html"
    fields = ["name", "theme", "location", "description", "start_date", "end_date"]
    success_url = reverse_lazy("liste_conferences")

# --- Vue pour modifier une conférence ---
class ConferenceUpdate(UpdateView):
    model = Conference
    template_name = "conferences/form.html"
    fields = ["name", "theme", "location", "description", "start_date", "end_date"]
    success_url = reverse_lazy("liste_conferences")


# --- Vue pour supprimer une conférence ---
class ConferenceDelete(DeleteView):
    model = Conference
    template_name = "conferences/delete.html"
    success_url = reverse_lazy("liste_conferences")