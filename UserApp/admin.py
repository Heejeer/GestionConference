from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import user, OrganizingCommitee 

admin.site.site_title = "Gestion Conférence 25/26"
admin.site.site_header = "Gestion Conférences"
admin.site.index_title = "django App Conférence"

@admin.register(user)
class CustomUserAdmin(UserAdmin):
    list_display = ('user_id', 'username', 'email', 'first_name', 'last_name', 'role', 'is_staff')
    ordering = ('last_name', 'first_name')
    list_filter = ('role',)
    search_fields = ('first_name', 'last_name')
    readonly_fields = ('user_id', 'created_at', 'update_at')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal Info'), {
            'fields': ('user_id', 'first_name', 'last_name', 'email', 'affiliation', 'nationality', 'role')
        }),
    )
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password', 'password2')
        }),
        (_('Personal Info'), {
            'fields': ('first_name', 'last_name', 'affiliation', 'nationality', 'role')
        }),
    )

@admin.register(OrganizingCommitee)
class AdminOrganizingCommiteeModel(admin.ModelAdmin):
    list_display = ("user", "conference", "commitee_role", "join_date")
    ordering = ("commitee_role",)
    list_filter = ("commitee_role",)
    search_fields = ("user__first_name", "user__last_name")
    date_hierarchy = "join_date"

    fieldsets = (
        ("Committee Assignment", {
            "fields": ("user", "conference", "commitee_role")
        }),
        ("Dates", {
            "fields": ("join_date",)
        }),
        
    )
    
    readonly_fields = ()