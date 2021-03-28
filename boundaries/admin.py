from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Boundary


class BoundaryAdmin(LeafletGeoAdmin):
    list_display = [
        "pk",
        "name",
        "adm1_pcode",
    ]


admin.site.register(Boundary, BoundaryAdmin)
