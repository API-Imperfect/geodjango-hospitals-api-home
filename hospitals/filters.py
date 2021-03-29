from boundaries.models import Boundary
from django_filters import rest_framework as filters
from rest_framework_gis.filterset import GeoFilterSet

from .models import Hospital


class HospitalsFilter(GeoFilterSet):
    province = filters.CharFilter(
        method="get_hospitals_by_province", lookup_expr="within"
    )

    class Meta:
        model = Hospital
        exclude = ["geom"]

    def get_hospitals_by_province(self, queryset, name, value):
        filtered_boundary = Boundary.objects.filter(pk=value)
        if filtered_boundary:
            boundary = filtered_boundary.first()
            return queryset.filter(geom__within=boundary.geom)
        return queryset
