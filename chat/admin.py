from django.contrib import admin
from chat.models import Satellite

class SatelliteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'orbital_state', 'designation',
					'orbit', 'created_at', 'updated_at')
    search_fields = ('name',)


admin.site.register(Satellite, SatelliteAdmin)
