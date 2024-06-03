from django.contrib import admin
from .models import josaaTable

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('Programme','Year')

admin.site.register(josaaTable,ServiceAdmin)