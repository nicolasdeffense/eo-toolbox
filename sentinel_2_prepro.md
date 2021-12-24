---
layout: sub_page
title: Sentinel-2 preprocessing 
---

[<img src="./buttons/view_button.png" width="100"/>](https://nicolasdeffense.github.io/eo-toolbox/notebooks/4_Sentinel_2_preprocessing/sentinel_2_prepro.html)

[<img src="./buttons/download_button.png" width="100"/>](https://nicolasdeffense.github.io/eo-toolbox/notebooks/4_Sentinel_2_preprocessing/sentinel_2_prepro.ipynb)

The *Copernicus Sentinel-2* mission comprises a constellation of two polar-orbiting satellites placed in the same sun-synchronous orbit, phased at 180° to each other. It aims at monitoring variability in land surface conditions, and its wide swath width (290 km) and high revisit time (10 days at the equator with one satellite, and 5 days with 2 satellites under cloud-free conditions which results in 2-3 days at mid-latitudes) will support monitoring of Earth's surface changes.

> Before strating this notebook, you should download a Sentinel-2 Level-2A product in <a href="https://scihub.copernicus.eu/dhus/#/home" target="_blank">Copernicus Open Access Hub</a>. The L2A products are downloadable by tiles which are 100x100 km2 ortho-images in UTM/WGS84 projection.

The different preprocessing step are as following :

1. Resample images at 20m to 10m (if you want to work with Red, Green, Blue, NIR bands)
2. Clip images to the extent of Region of Interest (ROI)
3. Apply Scene Classification map (SCL) on reflectance images to mask invalid pixels

<img src="./notebooks/4_Sentinel_2_preprocessing/figures/prepro_S2.png" width="1000">


