---
layout: sub_page
title: Sentinel-1 
---

# 1. Load Sentinel-1 GRD

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

## 1.2 Filter Sentinel-1 data

```js
// Define time period, polarisation and orbit direction
var startDate = '2019-01-01'
var endDate   = '2019-12-31'

var polarisation    = 'VV'
var orbit_direction = 'DESCENDING'
var instrument      = 'IW'
```

```js
// Select S1 IW images in area of interest and time period
var s1_filter = sentinel_1
                .filter(ee.Filter.eq('instrumentMode', instrument))
                .filter(ee.Filter.listContains('transmitterReceiverPolarisation', polarisation))
                .select(polarisation)
                .filter(ee.Filter.eq('orbitProperties_pass', orbitDirection))
                .filterDate(startDate, endDate)
                .filterBounds(roi)
```



# 2. Composite over a single time period 

Reducers are the way to aggregate data over time, space, bands, arrays and other data structures in Earth Engine. The `ee.Reducer` class specifies how data is aggregated. The reducers in this class can specify a simple statistic to use for the aggregation (e.g. minimum, maximum, mean, median, standard deviation, etc.), or a more complex summary of the input data (e.g. histogram, linear regression, list).

Reductions may occur over :
- **time (`imageCollection.reduce()`),**
- space (`image.reduceRegion()`, `image.reduceNeighborhood()`),
- bands (`image.reduce()`),
- attribute space of a `FeatureCollection`** (`featureCollection.reduceColumns()` or `FeatureCollection` methods that start with `aggregate_`).


Consider the example of needing to take the median over a time series of images represented by an `ImageCollection`. To reduce an `ImageCollection`, use `imageCollection.reduce()`. This reduces the collection of images to an individual image. Specifically, the output is computed pixel-wise, such that each pixel in the output is composed of the median value of all the images in the collection at that location. To get other statistics, such as mean, sum, variance, an arbitrary percentile, etc., the appropriate reducer should be selected and applied.

> For basic statistics like min, max, mean, etc., `ImageCollection` has shortcut methods like `min()`, `max()`, `mean()`, etc. They function in exactly the same way as calling `reduce()`, except the resultant band names will not have the name of the reducer appended.

**To composite images in an `ImageCollection`, use `imageCollection.reduce()`. This will composite all the images in the collection to a single image representing, for example, the min, max, mean or standard deviation of the images.**


<figure class="image">
    <img src="../figures/Reduce_ImageCollection.png" alt="Image classification" width="200">
    <figcaption>Illustration of an ee.Reducer applied to an ImageCollection.</figcaption>
</figure>


```js
var startPeriod = '2019-01-01'
var endPeriod   = '2019-03-31'
```

```js
// Compute mean over a period and clip to the ROI extent

var s1_mean = s1_filter
                    .filterDate(startPeriod, endPeriod)
                    .reduce(ee.Reducer.mean())
                    .clip(roi)
```

```js
// Compute standard deviation over a period and clip to the ROI extent

var s1_std  = s1_filter.
                    filterDate(startPeriod, endPeriod)
                    .reduce(ee.Reducer.stdDev())
                    .clip(roi)
```



## 2.1 Export one composite

```js
// Get projection of the original image
var projection = s1_filter.first().projection().getInfo()

// Export the image, specifying the CRS, transform, and region.
Export.image.toDrive({
  image: s1_mean,
  description: 'mean_Q1_Namur',
  folder: 'LBRAT2104',
  crs: projection.crs,                // The base coordinate reference system of this projection (e.g. 'EPSG:4326')
  crsTransform: projection.transform, // The transform between projected coordinates and the base coordinate system
  region: roi
});
```

> Composite images created by reducing an image collection are able to produce pixels in any requested projection and therefore have no fixed output projection. Instead, composites have the default projection of WGS-84 with 1-degree resolution pixels. Composites with the default projection will be computed in whatever output projection is requested. A request occurs by displaying the composite in the Code Editor or by explicitly specifying a projection/scale as in an aggregation such as `ReduceRegion` or `Export`.


# 3. Composite over mulitple time periods


```js
// List of months
var months = ee.List.sequence(1, 12)
print("Months : ",months)

// List of years
var years = ee.List.sequence(2019, 2019)
print("Years : ",years)
```

```js
// Use .map() to compute monthly composite and clip them to the ROI
var monthly_mean = ee.ImageCollection.fromImages(
  years.map(function (y) {
        return months.map(function (m) {
                return s1_filter
                        .filter(ee.Filter.calendarRange(y, y, 'year'))
                        .filter(ee.Filter.calendarRange(m, m, 'month'))
                        .reduce(ee.Reducer.mean())
                        .set('year',y)
                        .set('month',m);
            });
  })
  .flatten())
  .map(function(image){return image.clip(roi)})
```

[Source](https://gis.stackexchange.com/questions/387012/google-earth-engine-calculating-and-plotting-monthly-average-ndvi-for-a-region)


## 3.1 Export multiple composites (`imageCollection`)



```js
// Converts a collection to a single multi-band image containing all of the bands of every image in the collection.
var monthly_mean_image = monthly_mean.toBands()
```

```js
// Get projection of the original image
var projection = s1_filter.first().projection().getInfo()

// Export the image, specifying the CRS, transform, and region.
Export.image.toDrive({
  image: monthly_mean_image,
  description: 'monthly_mean_Namur_2019',
  folder: 'LBRAT2104',
  crs: projection.crs,
  crsTransform: projection.transform,
  region: roi
});
```

## 3.2 Visualization

```js
// Define arguments for animation function parameters.
var videoArgs = {
  dimensions: 800,
  region: roi.geometry(),
  framesPerSecond: 5,
  crs: 'EPSG:3857',
  min: -25.0,
  max: 5.0
};

print(ui.Thumbnail(monthly_mean, videoArgs));
print(monthly_mean.getVideoThumbURL(videoArgs));
```


<figure class="video_container">
  <video width="800" controls="true" allowfullscreen="true">
    <source src="../figures/s1_mean_mensuel_2019.mov" type="video/mp4">
  </video>
</figure>


[Source](https://developers.google.com/earth-engine/guides/ic_visualization)