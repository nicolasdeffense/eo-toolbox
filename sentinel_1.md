---
layout: sub_page
title: Sentinel-1 
---

# Load data

## Sentinel-1 GRD data

The Sentinel-1 mission provides data from a dual-polarization C-band Synthetic Aperture Radar (SAR) instrument at 5.405GHz (C band). This collection includes the S1 Ground Range Detected (GRD) scenes, processed using the Sentinel-1 Toolbox to generate a calibrated, ortho-corrected product. The collection is updated daily. New assets are ingested within two days after they become available.

```js
// Load Sentinel-1 GRD

var sentinel_1 = ee.ImageCollection("COPERNICUS/S1_GRD")
```

Each scene was pre-processed with Sentinel-1 Toolbox using the following steps:
1. Thermal noise removal
2. Radiometric calibration
3. Terrain correction using SRTM 30 or ASTER DEM for areas greater than 60 degrees latitude, where SRTM is not available
4. The final terrain-corrected values are converted to decibels via log scaling (10*log10(x)).

For more information about these pre-processing steps, please refer to the [Sentinel-1 Pre-processing article](https://developers.google.com/earth-engine/guides/sentinel1). For further advice on working with Sentinel-1 imagery, see [Guido Lemoine's tutorial](https://developers.google.com/earth-engine/tutorials/community/sar-basics) on SAR basics and [Mort Canty's tutorial](https://developers.google.com/earth-engine/tutorials/community/detecting-changes-in-sentinel-1-imagery-pt-1) on SAR change detection.

## ROI data

```js
var roi_geometry = ee.FeatureCollection("users/nicolasdeffense/extent_roi_32631")
```

# Filter Sentinel-1 data

```js
// Define time period, polarisation and orbit direction

var startDate = '2019-01-01'
var endDate = '2019-12-31'
var polarisation = 'VV'
var orbit_direction = 'DESCENDING'
var instrument = 'IW'
```

```js
// Select S1 IW images in area of interest and time period
var s1_filter = sentinel_1
                .filter(ee.Filter.eq('instrumentMode', instrument))
                .filter(ee.Filter.listContains('transmitterReceiverPolarisation', polarisation))
                .select(polarisation)
                .filter(ee.Filter.eq('orbitProperties_pass', orbit_direction));
                .filter(ee.Filter.date(startDate, endDate))
                .filterBounds(roi_geometry)
```

# Reducer

Reducers are the way to aggregate data over time, space, bands, arrays and other data structures in Earth Engine. The `ee.Reducer` class specifies how data is aggregated. The reducers in this class can specify a simple statistic to use for the aggregation (e.g. minimum, maximum, mean, median, standard deviation, etc.), or a more complex summary of the input data (e.g. histogram, linear regression, list).

Reductions may occur over :
- **time** (`imageCollection.reduce()`),
- **space** (`image.reduceRegion()`, `image.reduceNeighborhood()`),
- **bands** (`image.reduce()`),
- **attribute space of a `FeatureCollection`** (`featureCollection.reduceColumns()` or `FeatureCollection` methods that start with `aggregate_`).

## ImageCollection Reductions over time

Consider the example of needing to take the median over a time series of images represented by an `ImageCollection`. To reduce an `ImageCollection`, use `imageCollection.reduce()`. This reduces the collection of images to an individual image. Specifically, the output is computed pixel-wise, such that each pixel in the output is composed of the median value of all the images in the collection at that location. To get other statistics, such as mean, sum, variance, an arbitrary percentile, etc., the appropriate reducer should be selected and applied.

> For basic statistics like min, max, mean, etc., `ImageCollection` has shortcut methods like `min()`, `max()`, `mean()`, etc. They function in exactly the same way as calling `reduce()`, except the resultant band names will not have the name of the reducer appended.

<figure class="image">
    <img src="./figures/Reduce_ImageCollection.png" alt="Image classification" width="200">
    <figcaption>Illustration of an ee.Reducer applied to an ImageCollection.</figcaption>
</figure>


```js
// Compute mean and standard deviation over a period

var startPeriod = '2019-01-01'
var endPeriod   = '2019-01-31'

var s1_mean = s1_filter
                    .filterDate(startPeriod, endPeriod)
                    .reduce(ee.Reducer.mean())

var s1_std  = s1_filter.
                    filterDate(startPeriod, endPeriod)
                    .reduce(ee.Reducer.stdDev())
```