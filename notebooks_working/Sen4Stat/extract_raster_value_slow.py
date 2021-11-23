import geopandas as gpd
import rasterio
from rasterio.plot import show


point_shp   = '/export/projects/Sen4Stat/WORK/IN_SITU/SITE_41/SAMPLING_DESIGN_V25/SEN_2021_SITE_41_buf_0_LC_all_EXTENT_wall_to_wall_SEG_RATIO_100_LEVEL_grp_1_SD_25_cal_parcels_positions.shp'
classif_tif = '/export/projects/Sen4Stat/WORK/CLASSIF/SITE_41/06-01_11-15/RF_OpenCV/SAMPLING_DESIGN_V25/SEN_2021_SITE_41_buf_0_LC_all_EXTENT_wall_to_wall_SEG_RATIO_100_LEVEL_grp_1_SD_25_FEAT_2_CLASSIF_RF_OpenCV_v1_reclassify_grp_A_nb.tif'


val_point = gpd.read_file(point_shp)

print(val_point)

classif = rasterio.open(classif_tif)

y_true = []
y_pred = []

for i, row in val_point[0:200].iterrows():
    class_true = row['grp_A_nb']
    geom = row['geometry']
    x = geom.xy[0][0]
    y = geom.xy[1][0]

    row, col = classif.index(x,y)
    class_pred = classif.read(1)[row,col]
    
    y_true.append(class_true)
    y_pred.append(class_pred)

print(y_true)
print(y_pred)