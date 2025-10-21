from django.contrib import admin
from .models import Conference,Submission
# Register your models here.
admin.site.site_title="Gestion Conférence 25/26"
admin.site.site_header="Gestion Conférences"
admin.site.index_title="django App Conférence"

#admin.site.register(Conference)
admin.site.register(Submission)

class SubmissionInline(admin.StackedInline):
    model=Submission
    extra=1
    readonly_fields=("submission_date",)

@admin.action(description="marquer les soumissions comme payés")
def mark_as_payed(modeladmin,req,queryset):
    queryset.update(payed=True)
@admin.action
def mark_as_accepted(m,rq,q):
    q.update(status="accepted")

@admin.register(Conference)
class AdminconferenceModel(admin.ModelAdmin) :
    list_display=("name","theme","start_date","end_date","a")
    ordering=("start_date",)
    list_filter=("theme",)
    search_fields=("description","name")
    date_hierarchy="start_date"
    fieldsets=(
        ("Information general", {
            "fields":("cnference_id","name","theme","description")
        }),
        ("logistics Info", {
            "fields":("location","start_date","end_date")
        })
    )
    readonly_fields=("cnference_id",)
    def a(self,objet):
        if objet.start_date and objet.end_date :
            return (objet.end_date-objet.start_date).days
        return "RAS"
    a.short_description="Duration(days)"
    inlines=[SubmissionInline]
    aactions =[mark_as_payed,mark_as_accepted]
 