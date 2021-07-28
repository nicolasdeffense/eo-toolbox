"""
Create a .netrc file in your user home directory:

machine scihub.copernicus.eu
login <user>
password <password>
"""

from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import date
import pandas as pd


computer_path = '/Volumes/nbdid-sst-lbrat2104/'
grp_letter    = 'X'

# Directory for all work files
work_path = f'{computer_path}GROUP_{grp_letter}/WORK/'

roi_path = f'{work_path}ROI/'

roi_file_json = f'{roi_path}extent_roi_4326.geojson'


periods = [
    #(date(2020, 6, 1), date(2020, 6, 30)),
    #(date(2020, 7, 1), date(2020, 7, 31)),
    (date(2020, 8, 1), date(2020, 8, 31)),
    (date(2020, 9, 1), date(2020, 9, 30)),
    (date(2020, 10, 1), date(2020, 10, 31)),
]

# connect to the API

user     = 'ndeffense'
password = 'lbrat2104'

# Connect to the API

api = SentinelAPI(user, password)
#api = SentinelAPI(None, None, 'https://scihub.copernicus.eu/dhus')

# search by polygon, time, and Hub query keywords
footprint = geojson_to_wkt(read_geojson(roi_file_json))

for dates in periods:
    products = api.query(footprint,
                         date = dates,
                         platformname = 'Sentinel-2',
                         cloudcoverpercentage = (0, 90))

    # GeoPandas GeoDataFrame with the metadata of the scenes and the footprints as geometries
    dataframe = api.to_geodataframe(products)
    # Save as csv
    dataframe.to_csv(f's2query_{dates[0].strftime("%Y%m%d")}_{dates[1].strftime("%Y%m%d")}.csv')
