from django.contrib import admin
from .models import jossaTable

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('Programme','Year')

admin.site.register(jossaTable,ServiceAdmin)