from django.urls import path
from . import views
from .views import (
    ConferenceDetails,
    ConferenceCreate,
    ConferenceUpdate,
    ConferenceDelete,
    ConferenceList,
)

urlpatterns = [
    # Liste
    path("liste/",ConferenceList.as_view() , name="liste_conferences"),

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
