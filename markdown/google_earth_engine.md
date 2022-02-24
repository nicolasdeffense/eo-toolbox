---
layout: sub_page
title: Google Earth Engine
description: How to access Google Earth Engine ?
---

## What is Earth Engine?

Earth Engine is a platform for scientific analysis and visualization of geospatial datasets, for academic, non-profit, business and government users.

Earth Engine hosts satellite imagery and stores it in a public data archive that includes historical earth images going back more than forty years. The images, ingested on a daily basis, are then made available for global-scale data mining.

Earth Engine also provides APIs and other tools to enable the analysis of large datasets.

## How do I get access?

To get access to Earth Engine, please fill out the form at [signup.earthengine.google.com](https://signup.earthengine.google.com/). You will receive an email titled *"Welcome to Google Earth Engine"* with instructions for getting started.

## What datasets are available?

We have a searchable data catalog, including the entire EROS (USGS/NASA) Landsat catalog, numerous MODIS datasets, Sentinel-1 data, NAIP data, precipitation data, sea surface temperature data, CHIRPS climate data, and elevation data.

Users can also upload their own data for analysis in Earth Engine, with full control over access.

## Can I use my own proprietary imagery and vector data?

Yes. Earth Engine enables you to upload your own raster and vector data (e.g. GeoTIFF or Shape files) for analysis.

You can use the <a href="https://developers.google.com/earth-engine/guides/asset_manager"> Asset Manager</a> to upload datasets in the Shapefile or CSV format or to upload image or other georeferenced raster datasets in GeoTIFF or TFRecord format.

>Your uploaded assets are initially private, but can be shared as described in the <a href=https://developers.google.com/earth-engine/guides/asset_manager#sharing-assets> Sharing Assets Section</a>.

### Uploading table assets (shapefile, csv)

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

### Uploading image assets (GeoTIFF)

To upload a GeoTIFF using the Code Editor, select the Assets tab in the upper left corner, click the <img src="https://developers.google.com/earth-engine/images/Asset_manager_new_button.png"> button, then select <strong>Image upload</strong>.  Earth Engine presents an upload dialog which should look similar to Figure 1.  Click the <strong>SELECT</strong> button and navigate to a GeoTIFF on your local file system.

Give the image an appropriate asset ID (which doesn't already exist) in your user folder. If you'd like to upload the image into an existing folder or collection, prefix the asset ID with the folder or collection ID, for example <code translate="no" dir="ltr">/users/name/folder-or-collection-id/new-asset</code>.

Click <strong>UPLOAD</strong> to start the upload.

<figure>
<img alt="assets" src="https://developers.google.com/earth-engine/images/Asset_manager_upload_anon.png">
<figcaption>Figure 1. The asset manager image upload dialog</figcaption>
</figure>


---

[Google Earth Engine](https://earthengine.google.com/faq/)