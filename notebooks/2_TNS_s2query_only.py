from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import date
import pandas as pd


periods = [
    #(date(2020, 1, 1), date(2020, 2, 28)),
    #(date(2020, 3, 1), date(2020, 4, 30)),
    #(date(2020, 5, 1), date(2020, 6, 30)),
    #(date(2020, 7, 1), date(2020, 8, 31)),
    #(date(2020, 9, 1), date(2020, 10, 31)),
    (date(2020, 1, 1), date(2020, 12, 31)),
]
print(periods)

# connect to the API
api = SentinelAPI("bdelhez", "Bdelhez1$", 'https://scihub.copernicus.eu/dhus')

# search by polygon, time, and Hub query keywords
#folder="//geo12.elie.ucl.ac.be/root/homes/bdelhez/Script/SentinelDownload/"
folder="//geo12/homes/bdelhez/Script/SentinelDownload/"
footprint = geojson_to_wkt(read_geojson(folder+'TNS_extent.geojson'))

for dates in periods:
    print(f"date: {dates[0].strftime('%Y%m%d')} - {dates[1].strftime('%Y%m%d')}")
    products = api.query(footprint,
                         date = dates,
                         platformname = 'Sentinel-2',
                         processinglevel = 'Level-1C',
                         cloudcoverpercentage = (0, 50))

    # GeoPandas GeoDataFrame with the metadata of the scenes and the footprints as geometries
    #dataframe = api.to_geodataframe(products)
    # Save as csv
    #dataframe.to_csv(f'TNS_s2query_{dates[0].strftime("%Y%m%d")}_{dates[1].strftime("%Y%m%d")}.csv')
       
    # convert to Pandas DataFrame (without extent of each scene)
    products_df = api.to_dataframe(products)
    # Save as csv
    #products_df.to_csv(f'TNS_s2query_{dates[0].strftime("%Y%m%d")}_{dates[1].strftime("%Y%m%d")}.csv')
    # Save as xlsx
    products_df.to_excel(f'TNS_s2query_{dates[0].strftime("%Y%m%d")}_{dates[1].strftime("%Y%m%d")}.xls')
    
    # download all results from the search
    api.download_all(products)
