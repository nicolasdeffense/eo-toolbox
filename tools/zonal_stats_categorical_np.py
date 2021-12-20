import numpy as np
import rasterio
import rasterio.mask
import geopandas as gpd


raster_file = ''
vector_file = ''
vector_field = ''

gdf = gpd.read_file(vector_file)

src = rasterio.open(raster_file, "r")

for i in range(0,len(gdf))[0:10]:
    
    fid  = gdf.loc[i,vector_field]
    geom = gdf.geometry[[i]]
    print(f'ID : {fid}')

    # Crop the raster to the extent of the shape
    out_image, out_transform = rasterio.mask.mask(src, geom, crop=False)
    
    out_image = out_image[0]

    unique_elements, counts_elements = np.unique(out_image, return_counts=True)
    
    print(unique_elements)
    print(counts_elements)

src.close()