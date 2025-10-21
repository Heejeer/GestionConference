from django.urls import path
from . import views
from .views import (
    ConferenceDetails,
    ConferenceCreate,
    ConferenceUpdate,
    ConferenceDelete,
)

urlpatterns = [
    # Liste
    path("liste/", views.liste_conferences, name="liste_conferences"),

    # Détails
    path("<int:pk>/", ConferenceDetails.as_view(), name="conference_details"),

    # Ajouter
    path("ajouter/", ConferenceCreate.as_view(), name="conference_create"),

    # Modifier
    path("<int:pk>/modifier/", ConferenceUpdate.as_view(), name="conference_update"),

    # Supprimer
    path("<int:pk>/supprimer/", ConferenceDelete.as_view(), name="conference_delete"),

    # Redirection si "details/" sans pk
    path("details/", views.details_index, name="details_index"),
]
