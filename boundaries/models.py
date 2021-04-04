from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _


class Boundary(models.Model):
    adm0_en = models.CharField(max_length=254)
    adm0_sw = models.CharField(max_length=254)
    adm0_pcode = models.CharField(max_length=254)
    name = models.CharField(_("Boundary Name"), max_length=254)
    adm1_rw = models.CharField(max_length=254)
    adm1_pcode = models.CharField(_("Boundary Code"), max_length=254)

    # set geometry field to be MultiPolygonField
    # with Spatial Reference System Identity
    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        verbose_name_plural = "Boundaries"

    def __str__(self):
        return self.name
