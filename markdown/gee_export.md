---
layout: sub_page
title: Export data
description: from Google Earth Engine
---


# Export a single image

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


# Export an Image Collection


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