from django.db import models
from ConferenceApp.models import Conference
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
# Create your models here.    

room_validator= RegexValidator(
    regex=r'^[A-Za-z0-9]+$',
    message="ce champs ne doit contenir que des lettres et des chiffres"
)

class Session(models.Model) :
    session_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    topic=models.CharField(max_length=255)
    session_day=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()
    room=models.CharField(max_length=255,validators=[room_validator])
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    conference=models.ForeignKey(Conference,on_delete=models.CASCADE,related_name="sessions")
    def clean(self) :
        if self.session_day and self.conference :
            if not (self.conference.start_date <= self.session_day <= self.conference.ens_date):
                raise ValidationError(" la date de la session doit appartenir à l intervalle de dates de la conférence associée")
    def clean(self):
        if self.start_time and self.end_time :
            if not self.start_time.hour < self.end_time.hour :
                raise ValidationError("l heure de fin doit etre supérieur à l heure de debut")

    