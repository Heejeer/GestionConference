from django.contrib import admin
from .models import Session 
from datetime import datetime, date, timedelta

admin.site.site_title = "Gestion Conférence 25/26"
admin.site.site_header = "Gestion Conférences"
admin.site.index_title = "django App Conférence"

@admin.register(Session)
class AdminSessionModel(admin.ModelAdmin):
    list_display = ("title", "topic", "session_day", "start_time", "end_time", "room", "conference", "duration_minutes")
    ordering = ("session_day",)
    list_filter = ("topic",)
    search_fields = ("title", "topic", "room")
    date_hierarchy = "session_day"
    
    fieldsets = (
        ("Session Details", {
            "fields": ("session_id", "title", "topic", "conference")
        }),
        ("Schedule and Location", {
            "fields": ("session_day", "start_time", "end_time", "room")
        }),
    )
    readonly_fields = ("session_id",) 

    def duration_minutes(self, obj):
        if obj.start_time and obj.end_time:
        # Convertir en minutes depuis minuit
            start_minute = obj.start_time.hour * 60 + obj.start_time.minute
            end_minute = obj.end_time.hour * 60 + obj.end_time.minute
        
        # Durée en minutes
            total_minute =abs( end_minute - start_minute )
            hours = total_minute // 60
            minutes = total_minute % 60
        
            return f"{hours}h {minutes:02d}m"
