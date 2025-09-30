from django.contrib import admin
from .models import Service, ServiceRequest

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # adjust fields based on your model
    search_fields = ('name',)

class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'service', 'status', 'created_at')
    list_filter = ('status', 'service')
    search_fields = ('user__username', 'description')
    readonly_fields = ('created_at',)

admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceRequest, ServiceRequestAdmin)
