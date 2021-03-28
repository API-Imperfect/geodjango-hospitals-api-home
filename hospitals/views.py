from rest_framework import viewsets

from .filters import HospitalsFilter
from .models import Hospital
from .serializers import HospitalSerializer


class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    filterset_class = HospitalsFilter
