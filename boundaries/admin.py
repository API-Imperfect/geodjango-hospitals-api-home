from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Boundary


class BoundaryAdmin(LeafletGeoAdmin):
    list_display = ["name"]


admin.site.register(Boundary, BoundaryAdmin)
