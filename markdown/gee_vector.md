---
layout: sub_page
title: Import data in Google Earth Engine
---

You can use the [Asset Manager](href="https://developers.google.com/earth-engine/guides/asset_manager") to upload datasets in the Shapefile or CSV format or to upload image or other georeferenced raster datasets in GeoTIFF or TFRecord format.

>Your uploaded assets are initially private, but can be shared as described in the [Sharing Assets Section](https://developers.google.com/earth-engine/guides/asset_manager#sharing-assets).

## Uploading table assets (shapefile, csv)

To upload a Shapefile from the Code Editor, click the <img src="https://developers.google.com/earth-engine/images/Asset_manager_new_button.png"> button, then select <strong>Shape files</strong> under the <strong>Table Upload</strong> section. An upload dialog similar to Figure 1 will be presented. Click the <strong>SELECT</strong> button and navigate to a Shapefile or Zip archive containing a Shapefile on your local file system.  When selecting a .shp file, be sure to select the related .dbf, .shx and .prj files.  Earth Engine will default to WGS84 (longitude, latitude) coordinates if a .prj file is not provided. If you are uploading a Zip archive, make sure it contains only one Shapefile (set of .shp, .dbf, .shx, .prj, etc.) and no duplicate filenames.  Make sure filenames do not include additional periods or dots. (Filenames will include a single period before
the extension.)

Give the table an appropriate asset ID (which doesn't already exist) in your
user folder. Click <strong>UPLOAD</strong> to start the upload.

<figure>
<img alt="assets" src="https://developers.google.com/earth-engine/images/Asset_manager_shp_upload.png">
<figcaption>Figure 1. The Asset Manager Shapefile upload dialog.  Note that the .shp, .dbf,
and .shx files are required. The other sidecar files are optional.  If the .prj file is not
provided, WGS84 is assumed.</figcaption>
</figure>


```js
var roi = ee.FeatureCollection("users/nicolasdeffense/extent_roi_32631")
```

## Datasets present in Google Earth engine


You can also use the datasets present in Google Earth engine. For instance, the [FAO *Global Administrative Unit Layers*](https://developers.google.com/earth-engine/datasets/tags/fao) (GAUL) compiles and disseminates the best available information on administrative units for all the countries in the world, providing a contribution to the standardization of the spatial dataset representing administrative units. Check this [website](https://data.apps.fao.org/catalog/dataset/gaul-codes) to easily find the code of the country/region you want to work on.


```js
// Import Belgium boundary
var fao_level0 = ee.FeatureCollection("FAO/GAUL/2015/level0")
var belgium = fao_level0.filter("ADM0_NAME == 'Belgium'")

// Import Walloon Region boundary
var fao_level1 = ee.FeatureCollection("FAO/GAUL/2015/level1")
var wallonia = fao_level1.filter("ADM1_CODE == 602")
```



## Uploading image assets (GeoTIFF)

To upload a GeoTIFF using the Code Editor, select the Assets tab in the upper left corner, click the <img src="https://developers.google.com/earth-engine/images/Asset_manager_new_button.png"> button, then select <strong>Image upload</strong>.  Earth Engine presents an upload dialog which should look similar to Figure 1.  Click the <strong>SELECT</strong> button and navigate to a GeoTIFF on your local file system.

Give the image an appropriate asset ID (which doesn't already exist) in your user folder. If you'd like to upload the image into an existing folder or collection, prefix the asset ID with the folder or collection ID, for example <code translate="no" dir="ltr">/users/name/folder-or-collection-id/new-asset</code>.

Click <strong>UPLOAD</strong> to start the upload.

<figure>
<img alt="assets" src="https://developers.google.com/earth-engine/images/Asset_manager_upload_anon.png">
<figcaption>Figure 1. The asset manager image upload dialog</figcaption>
</figure>