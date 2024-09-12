from django.contrib import admin
from .models import BugReport, AccountRequest

class MyAdminSite(admin.AdminSite):
    site_header = "CID Admin"
    site_title = "Configuration Item Database App Admin"
    index_title = "Welcome to CID Admin"

admin_site = MyAdminSite(name='admin')

@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('message', 'name', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('title', 'message')

@admin.register(AccountRequest)
class AccountRequestAdmin(admin.ModelAdmin):
    list_display = ('lastname', 'firstname', 'email', 'created_at', 'is_processed')
    list_filter = ('is_processed',)
    search_fields = ('lastname', 'email')
    actions = ['mark_as_processed']

    def mark_as_processed(self, request, queryset):
        queryset.update(is_processed=True)
    mark_as_processed.short_description = "Mark selected Requests as processed"