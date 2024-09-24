from django.contrib import admin
from .models import BugReport, AccountRequest, MaintTicket

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

@admin.register(MaintTicket)
class MaintTicketAdmin(admin.ModelAdmin):
    list_display = ('platform', 'username', 'description', 'status', 'created_at')
    list_filter = ('platform',)
    search_fields = ('platform', 'status')
    actions = ['mark_as_entered', 'mark_as_approved',]

    def mark_as_entered(self, request, queryset):
        queryset.update(status="entered")
    mark_as_entered.short_description = "Mark selected Requests as Entered"

    def mark_as_approved(self, request, queryset):
        queryset.update(status="approved")
    mark_as_approved.short_description = "Mark selected Requests as Approved"
