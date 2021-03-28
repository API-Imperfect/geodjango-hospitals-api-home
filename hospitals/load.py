from pathlib import Path

from django.contrib.gis.utils import LayerMapping

from .models import Hospital

hospital_mapping = {
    "name": "Hospital",
    "lon": "Long",
    "lat": "Lat",
    "fid": "FID",
    "geom": "POINT",
}

hospital_shp = Path(__file__).resolve().parent / "data" / "Hospitals.shp"


def run(verbose=True):
    # transform=False the data doesn't need to be converted. Its already
    # in WGS84(SRID=4326)
    lm = LayerMapping(Hospital, str(hospital_shp), hospital_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
