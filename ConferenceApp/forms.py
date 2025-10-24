from django import forms
from .models import Conference
class ConferenceForm(forms.ModelForm):
    class Meta:
        model=Conference
        fields=['name','theme','location','description','start_date','end_date']
        labels={
            'name':"titre de la conférence",
            'theme':"Thématique de la conférence",
        }
        widgets={
            'name':forms.TextInput(
                attrs={
                    'placeholder':"Entrer un titre à la conférence"
                }
            ),
            'start_date':forms.DateInput(
                attrs={
                    'type':"date"
                }
            ),
            'end_date':forms.DateInput(
                attrs={
                    'type':"date"
                }
            )
        }
