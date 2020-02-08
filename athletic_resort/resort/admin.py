from django.contrib import admin
from .models import resort_room, notepad

# Register your models here.
admin.site.site_header = 'Athletic Resort'

class ResortRoomAdmin(admin.ModelAdmin):
    list_display = 'room_type', 'resort_name', 'price'
    list_filter =  'resort_name', 'price', 'capacity', 'room_type',
    search_fields = 'room_type', 'price'
admin.site.register(resort_room, ResortRoomAdmin)

admin.site.register(notepad)