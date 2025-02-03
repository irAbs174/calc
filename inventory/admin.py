from django.contrib import admin
from .models import inventory

@admin.register(inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('inventory_id', 'inventory_name', 'inventory_capacity', 'inventory_location', 'personnal_id', 'created_at', 'updated_at')
    search_fields = ('inventory_name', 'inventory_id', 'inventory_location')
    list_filter = ('created_at', 'updated_at')