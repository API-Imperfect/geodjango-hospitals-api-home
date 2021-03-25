from pathlib import Path

from django.contrib.gis.utils import LayerMapping

from .models import Boundary

rwandaborder_mapping = {
    "adm0_en": "ADM0_EN",
    "adm0_sw": "ADM0_SW",
    "adm0_pcode": "ADM0_PCODE",
    "name": "ADM1_EN",
    "adm1_rw": "ADM1_RW",
    "adm1_pcode": "ADM1_PCODE",
    "geom": "MULTIPOLYGON",
}

boundary_shp = (
    Path(__file__).resolve().parent / "data" / "rwa_adm1_2006_NISR_WGS1984_20181002.shp"
)


def run(verbose=True):
    lm = LayerMapping(
        Boundary, str(boundary_shp), rwandaborder_mapping, transform=False
    )
    lm.save(strict=True, verbose=verbose)
