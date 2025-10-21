from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.utils import timezone
import uuid

# Create your models here.
class Conference(models.Model) :
    cnference_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    THEME=[
        ("IA","Computer science & Artificial Intelligence"),
        ("SE","Science & Engineering"),
        ("SC"," Social Sciences & Education"),
        ("IT","Interdisciplinary Themes"),
    ]
    theme=models.CharField(max_length=255,choices=THEME)
    location=models.CharField(max_length=50)
    description=models.TextField(validators=[MinLengthValidator(30,"description trop court !")])
    start_date=models.DateField()
    end_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def clean(self):
        if self.start_date and self.end_date :
            if self.start_date > self.end_date:
                raise ValidationError("la date de début doit etre inférieur à la date de fin")

def validate_max_keywords(value):
    keywords = [k.strip() for k in value.split(',') if k.strip()]
    max_keywords = 10
    if len(keywords) > max_keywords:
        raise ValidationError(
            f'Vous ne pouvez pas avoir plus de {max_keywords} mots-clés. '
            f'Actuellement : {len(keywords)}.'
        )
    """
    keysword_list = ""
    for k in self.keyswords.split(','):
        k = k.strip()
        if k :
            keysword_list.append(k)
    if len(keysword_list) > 3 :
        raise ValidationError("vous aves plus de 10 mots !"

    """
def generate_submission_id():
    uid = str(uuid.uuid4()).replace("-", "").upper()  
    letters_only = ''.join([ch for ch in uid if ch.isalpha()]) 
    return "SUB-" + letters_only[:8]  

class Submission(models.Model) :
    submission_id=models.CharField(max_length=12,primary_key=True,unique=True,default=generate_submission_id)
    title=models.CharField(max_length=50)
    abstract=models.TextField()
    keyswords=models.TextField(validators=[validate_max_keywords])
    paper=models.FileField(
        upload_to="papers/",
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
    )
    STATUS=[
        ("submitted","submitted"),
        ("uder review","under review"),
        ("accepted","accepted"),
        ("rejeted","rejected"),
    ]
    status=models.CharField(max_length=50,choices=STATUS)
    payed=models.BooleanField(default=False)
    submission_date=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey("UserApp.User",on_delete=models.CASCADE,related_name="submissions")
    conference=models.ForeignKey(Conference,on_delete=models.CASCADE,related_name="submissions")
    def save(self, *args, **kwargs):
        if not self.submission_id:
            self.submission_id = generate_submission_id()
        super().save(*args, **kwargs)

    def clean(self):
    
        if self.conference.cnference_id:
            try:
                conference = self.conference
                today = timezone.now().date()
                if conference.start_date < today and self.submission_date > conference.start_date :
                    raise ValidationError("Vous ne pouvez pas soumettre pour une conférence déjà passée.")
            except Conference.DoesNotExist:
                pass  
        
        if self.user.user_id:
            now = timezone.now()
            today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
            today_end = now.replace(hour=23, minute=59, second=59, microsecond=999999)

            submissions_today = Submission.objects.filter(
                user=self.user,
                submission_date__range=(today_start, today_end)
            )

        if self.pk:
            submissions_today = submissions_today.exclude(pk=self.pk)

        if submissions_today.count() >= 3:
            raise ValidationError("Vous ne pouvez pas soumettre plus de 3 conférences par jour.")