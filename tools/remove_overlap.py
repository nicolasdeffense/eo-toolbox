#!/usr/bin/python3

import geopandas as gpd

# ------------------------------------------------------------------------

def remove_overlap(gdf, id_column='id'):
    
    gdf_out = gdf.copy()
    
    gdf_out.geometry = gdf_out.buffer(0)
    
    id_poly = gdf[id_column].unique()
    
    res = gpd.overlay(gdf, gdf, how='intersection')
    
    for idx in id_poly:
        overlap_serie = res.loc[(res[id_column+'_1']==idx) & (res[id_column+'_2']!=idx)]
        
        for i, row in overlap_serie.iterrows():
            gdf_out.loc[gdf_out[id_column]==idx, 'geometry'] = gdf_out.loc[gdf_out[id_column]==idx, 'geometry'].difference(row['geometry'])
    
    return gdf_out