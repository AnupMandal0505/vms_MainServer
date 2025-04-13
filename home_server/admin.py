from django.contrib import admin
from django.http import HttpResponse
import csv
from .models.user import ClientUser,UserLimitHistory
from home_server.models.account import ManageAccount, RequestLog  # Import models
from django.contrib.auth.admin import UserAdmin


# Register the model with admin panel
@admin.register(ClientUser)
class ClientUserAdmin(UserAdmin):
    model = ClientUser
    list_display = ('username', 'first_name', 'last_name',  'company_name', 'email', 'phone', 'limits' ,'is_active', 'date_joined', 'get_groups')
    search_fields = ('username', 'first_name', 'last_name',  'company_name', 'email', 'phone')
    ordering = ("phone",)
    readonly_fields=("date_joined",)
    fieldsets = (
        (None, {"fields": ("phone",)}),
        (("Personal info"), {"fields": ("first_name",'username', 'last_name',  "email", 'limits','company_name','address')}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),

        (("Group"), {"fields": ("groups","user_permissions")}),

        (("Reset Password"), {"fields": ("password",)}),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("phone", "usable_password", "password1", "password2"),
            },
        ),
    )

# Ensure get_groups is defined within the class
    def get_groups(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])
    
    get_groups.short_description = "Groups"  # Column name in admin panel
    actions = ['export_as_csv']  # Add CSV export button

    def export_as_csv(self, request, queryset):
        """Export selected data as CSV"""
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=home_servers.csv'
        
        writer = csv.writer(response)
        writer.writerow(['Company_name', 'Email', 'Phone', 'first_name', 'last_name',  'Max Users', 'Active', 'Created At'])
        
        for obj in queryset:
            writer.writerow([obj.company_name, obj.email, obj.phone, obj.first_name,  obj.last_name, obj.limits, obj.is_active, obj.date_joined])
        
        return response

    export_as_csv.short_description = "Download CSV (selected records)"



@admin.register(UserLimitHistory)
class UserLimitHistoryAdmin(admin.ModelAdmin):
    list_display = ('account', 'transaction_type', 'new_limit', 'timestamp')
    list_filter = ('transaction_type', 'timestamp')
    search_fields = ('account__username', 'transaction_type', 'new_limit')

    fieldsets = (
        ('Account Information', {'fields': ('account',)}),
        ('Transaction Details', {'fields': ('transaction_type', 'new_limit')}),
        ('Timestamp', {'fields': ('timestamp',)}),
    )

    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={meta}.csv'
        writer = csv.writer(response)

        writer.writerow(field_names)  # Write headers
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected as CSV"





# 🔹 Register ManageAccount Admin
@admin.register(ManageAccount)
class ManageAccountAdmin(admin.ModelAdmin):
    list_display = ('phone', 'client_user', 'otp','is_on_hold','delete_account')
    search_fields = ('phone', 'client_user__name','delete_account')
    list_filter = ('is_on_hold','delete_account')
    readonly_fields = ('id','pass_key')
    
    fieldsets = (
        ("Account Info", {'fields': ('phone', 'pass_key', 'client_user')}),
        ("Status", {'fields': ('is_on_hold','delete_account')}),
    )

    actions = ['export_as_csv']  # Add CSV export button


    def export_as_csv(self, request,queryset):
        """Generate CSV file for ManageAccounts"""
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=user_accounts.csv'

        writer = csv.writer(response)
        writer.writerow(['phone', 'Home Server', 'On Hold','Delete Account'])

        for obj in queryset:
            writer.writerow([obj.phone, obj.client_user.company_name, obj.is_on_hold, obj.delete_account])

        return response
    
    export_as_csv.short_description = "Download CSV (selected records)"


   


# 🔹 Register RequestLog Admin
@admin.register(RequestLog)
class RequestLogAdmin(admin.ModelAdmin):
    list_display = ('client_user', 'request_type', 'status', 'created_at')
    # search_fields = ('client_user__name', 'request_type')
    # list_filter = ('request_type', 'status')
    # readonly_fields = ('id', 'created_at')

    # fieldsets = (
    #     ("Request Details", {'fields': ('client_user', 'request_type', 'note')}),
    #     ("Status", {'fields': ('status',)}),
    #     ("Timestamps", {'fields': ('created_at',)}),
    # )

    # actions = ['export_as_csv']  # Add CSV export button


    # def export_as_csv(self, request,queryset):
    #     """Generate CSV file for Request Logs"""
    #     response = HttpResponse(content_type='text/csv')
    #     response['Content-Disposition'] = 'attachment; filename=request_logs.csv'

    #     writer = csv.writer(response)
    #     writer.writerow(['Home Server', 'Request Type', 'Note', 'Status', 'Created At'])

    #     for obj in queryset:
    #         writer.writerow([obj.client_user.name, obj.request_type, obj.note, obj.status, obj.created_at])

    #     return response

    # export_as_csv.short_description = "Download CSV (selected records)"
