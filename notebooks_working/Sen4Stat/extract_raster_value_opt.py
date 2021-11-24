import rasterio
import ogr
import time
from sklearn.metrics import confusion_matrix


point_shp   = '/export/projects/Sen4Stat/WORK/IN_SITU/SITE_41/SAMPLING_DESIGN_V25/SEN_2021_SITE_41_buf_0_LC_all_EXTENT_wall_to_wall_SEG_RATIO_100_LEVEL_grp_1_SD_25_val_parcels_positions.shp'
classif_tif = '/export/projects/Sen4Stat/WORK/CLASSIF/SITE_41/06-01_11-15/RF_OpenCV/SAMPLING_DESIGN_V25/SEN_2021_SITE_41_buf_0_LC_all_EXTENT_wall_to_wall_SEG_RATIO_100_LEVEL_grp_1_SD_25_FEAT_2_CLASSIF_RF_OpenCV_v1_reclassify_grp_A_nb.tif'

start_time = time.time()

raster = rasterio.open(classif_tif)
val = raster.read(1)

ds = ogr.Open(point_shp)
lyr = ds.GetLayer(0)


y_true = []
y_pred = []

for f in lyr:
        
    class_true = f.GetField("grp_A_nb")
    geo = f.geometry()
    x = geo.GetX()
    y = geo.GetY()

    row, col   = raster.index(x,y)
    class_pred = val[row,col]
    
    y_true.append(class_true)
    y_pred.append(class_pred)


cm = confusion_matrix(y_true, y_pred)

print(cm)

end_time = time.time()

time_elapsed = (end_time - start_time)

print(time_elapsed)