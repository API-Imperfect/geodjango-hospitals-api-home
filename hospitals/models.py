from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _


class Hospital(models.Model):
    name = models.CharField(_("Hospital Name"), max_length=100)
    lon = models.FloatField(_("Longitude"))
    lat = models.FloatField(_("Latitude"))
    fid = models.IntegerField(_("Field ID"))

    # GeoDjango-specific: a geometry field (MultiPointField)
    mpoly = models.MultiPointField()

    def __str__(self):
        return self.name
