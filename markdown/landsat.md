---
layout: sub_page
title: Landsat
description: with Google Earth Engine
---

# 1. Load Landsat Collection

Landsat, a joint program of the USGS and NASA, has been observing the Earth continuously from 1972 through the present day. Today the Landsat satellites image the entire Earth's surface at a 30-meter resolution about once every two weeks, including multispectral and thermal data.

Landsat data is available in Earth Engine in its raw form, as Surface Reflectance, TOA-corrected reflectance, and in various ready-to-use computed products such as NDVI and EVI vegetation indices.

> In this course we will only work with **Landsat Collection 2** that marks the second major reprocessing effort on the Landsat archive by the USGS that results in several data product improvements over Collection 1 that harness recent advancements in data processing and algorithm development.

|Satellite | Landsat 5  | Landsat 7   | Landsat 8  | Landsat 9 |
|----------|:----------: |:----------:|:---------: | :--------:|
|**Instrument** | <font size="2"> Multispectral Scanner (MSS), <br/>Thematic Mapper (TM) </font>|  <font size="2"> Enhanced Thematic Mapper <br/> (ETM+) </font>| <font size="2"> Operational Land Imager (OLI),<br/> Thermal Infrared <br/>Sensor (TIRS)</font>|  <font size="2"> OLI-2, TIRS-2 </font>|
|**Number of bands**| 10 | 10 | 10 | 10 |
|**Spatial resolution**| 30m x 30m | 30m x 30m| 30m x 30m | 30m x 30m
|**Temporal resolution**| 16 days |  16 days |  16 days |  16 days 
|**Temporal range**| 1984 - 2012 |1999 - Present| 2013 - Present | 2021 - Present
|**Google Earth Engine collection** | [Dataset](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LT05_C02_T1_L2) | [Dataset](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C02_T1_L2) | [Dataset](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C02_T1_L2)| *Not available* |


Let's define which datasets we will work with.

```js
// Load USGS Landsat 5 Level 2, Collection 2, Tier 1
var landsat_5 = ee.ImageCollection("LANDSAT/LT05/C02/T1_L2")

// Load USGS Landsat 7 Level 2, Collection 2, Tier 1
var landsat_7 = ee.ImageCollection("LANDSAT/LE07/C02/T1_L2")

// Load USGS Landsat 8 Level 2, Collection 2, Tier 1
var landsat_8 = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
```

## 1.1 Filter Landsat data


```js
// Define time period
var startDate = '2019-01-01'
var endDate   = '2019-12-31'
```

```js
// Select Landsat 8 images in area of interest and time period
var l8_filter = landsat_8
                .filterDate(startDate, endDate)
                .filterBounds(roi)
```

## 1.2 Apply scaling factors

A scale factor must be applied to both Collection 1 and Collection 2 Landsat Level-2 surface reflectance and surface temperature products before using the data.  
**Landsat Collection 2** have the following scale factors, fill values, data type, and valid range.


<figure class="responsive-figure-table"><table>
<thead>
<tr>
<th>Science Product</th>
<th>Scale Factor</th>
<th>Fill Value</th>
<th>Data Type</th>
<th>Valid Range</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://www.usgs.gov/core-science-systems/nli/landsat/landsat-collection-2-surface-reflectance">Surface Reflectance</a></td>
<td>0.0000275 + -0.2</td>
<td>0</td>
<td>Unsigned 16-bit integer</td>
<td>1-65455</td>
</tr>
<tr>
<td><a href="https://www.usgs.gov/core-science-systems/nli/landsat/landsat-collection-2-surface-temperature">Surface Temperature</a></td>
<td>0.00341802 + 149.0</td>
<td>0</td>
<td>Unsigned 16-bit integer</td>
<td>1-65455</td>
</tr>
</tbody>
</table></figure>


>**Examples for scaling Landsat Collection 2 Level-2 science products**  
> <font size="2">Landsat Collection 2 surface reflectance has a scale factor of 0.0000275 and an additional offset of -0.2 per pixel. <br/> For example, a pixel value of 18,639 is multiplied by 0.0000275 for the scale factor and then -0.2 is added for the additional offset to get a reflectance value of 0.313 after the scale factor is applied. </font>


```js
// Applies scaling factors.
function applyScaleFactors(image) {
  var opticalBands = image.select('SR_B.').multiply(0.0000275).add(-0.2)
  var thermalBands = image.select('ST_B.*').multiply(0.00341802).add(149.0)
  return image.addBands(opticalBands, null, true)
              .addBands(thermalBands, null, true)
}

var l8_filter = l8_filter.map(applyScaleFactors)
```


# 2. Cloud Mask

Most optical satellite imagery products come with one or more QA-bands that allows the user to assess quality of each pixel and extract pixels that meet their requirements. The most common application for QA-bands is to extract information about cloudy pixels and mask them. But the QA bands contain a wealth of other information that can help you remove low quality data from your analysis. Typically the information contained in QA bands is stored as Bitwise Flags. [More info about bitmasks](https://spatialthoughts.com/2021/08/19/qa-bands-bitmasks-gee/)

In Landsat imagery, pixel quality assessment (QA_PIXEL) bands are generated by the CFMask algorithm. Different bit definitions are used because the cirrus band is only available on Landsat 8 and 9. This band is relevant to both Surface Reflectance and Surface Temperature products.


|Bit | Landat 5 & 7 |Landsat 8 & 9 | 
|---------|:----------: |:----------:|
|0 | Fill | Fill |
|1 | Dilated Cloud|Dilated Cloud|
|2|Unused|Cirrus|
|3|Cloud|Cloud|
|4|Cloud Shadow|Cloud Shadow|
|5|Snow|Snow|
|6|Clear|Clear|
|7|Water|Water|
|8-9|Cloud Confidence|Cloud Confidence|
|10-11|Cloud Shadow Confidence|Cloud Shadow Confidence|
|12-13|Snow/Ice Confidence|Snow/Ice Confidence|
|14-15|Unused|Cirrus Confidence| 

The two following functions will be used to mask clouds, cloud shadows, ... on everny images of an `ImageCollection`.

```js
/**
 * Utility to extract bitmask values. 
 * Look up the bit-ranges in the catalog.
 * 
 * value - ee.Number or ee.Image to extract from.
 * fromBit - int or ee.Number with the first bit.
 * toBit - int or ee.Number with the last bit (inclusive). 
 *         Defaults to fromBit.
 */
function bitwiseExtract(value, fromBit, toBit) {
  if (toBit === undefined) toBit = fromBit
  var maskSize = ee.Number(1).add(toBit).subtract(fromBit)
  var mask = ee.Number(1).leftShift(maskSize).subtract(1)
  return value.rightShift(fromBit).bitwiseAnd(mask)
}
```


```js
var maskClouds = function(image) {
  var QA = image.select('QA_PIXEL');
  var clouds        = bitwiseExtract(QA, 3).eq(0)
  var cloud_shadows = bitwiseExtract(QA, 4).eq(0)
  var mask = clouds
              .and(cloud_shadows)
  var maskedImage = image.updateMask(mask)
  return maskedImage
}
```

# 3. Composites

## 3.1 Single period composite


```js
var l8_composite = l8_filter
                  .map(maskClouds)
                  .median()
```

## 3.2 Multiple period composites

```js
// List of months
var months = ee.List.sequence(1, 12)
print("Months : ",months)

// List of years
var years = ee.List.sequence(2019, 2019)
print("Years : ",years)

var monthly_mean = ee.ImageCollection.fromImages(
  years.map(function (y) {
        return months.map(function (m) {
                return l8_filter
                        .filter(ee.Filter.calendarRange(y, y, 'year'))
                        .filter(ee.Filter.calendarRange(m, m, 'month'))
                        .map(maskClouds)
                        .median()
                        .set('year',y)
                        .set('month',m);
            });
  })
  .flatten())
  .map(function(image){return image.clip(roi)})


print("Monthly mean : ",monthly_mean)
```

# 4. Visualization

```js
var visParams = {
  bands: ['SR_B4', 'SR_B3', 'SR_B2'],
  min: 0.0,
  max: 0.3,
}
```

## 4.1 Visualize single image

```js
Map.centerObject(roi, 8)
Map.addLayer(l8_composite, visParams, 'True Color (432) - Mask - Median')
```

## 4.2 Visualize imageCollection


```js
// Create RGB visualization images for use as animation frames.
var rgbVis = monthly_mean.map(function(img) {
  return img.visualize(visParams);
})

// Define GIF visualization arguments.
var gifParams = {
  region: roi.geometry(),
  dimensions: 1000,
  crs: 'EPSG:3857',
  framesPerSecond: 1,
  format: 'gif'
}

// Print the GIF URL to the console.
print(rgbVis.getVideoThumbURL(gifParams))

// Render the GIF animation in the console.
print(ui.Thumbnail(rgbVis, gifParams))
```


---

[Digital Earth Africa](https://docs.digitalearthafrica.org/en/latest/data_specs/Landsat_C2_SR_specs.html)

[bitwiseExtract function](https://gis.stackexchange.com/questions/349371/creating-cloud-free-images-out-of-a-mod09a1-modis-image-in-gee/349401#349401)