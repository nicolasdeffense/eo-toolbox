---
layout: sub_page
title: Sentinel-1 
---

## Load Sentinel-1 GRD data

{% highlight javascript %}
// load Sentinel-1 
var sentinel_1 = ee.ImageCollection("COPERNICUS/S1_GRD")

{% endhighlight %} 

---

```js
// load Sentinel-1 
var sentinel_1 = ee.ImageCollection("COPERNICUS/S1_GRD")
```




## Filter

```js
var year = '2019'
var polarisation = 'VV'
var orbit_direction = 'DESCENDING'

var s1_filterd = sentinel_1
                .filter(ee.Filter.eq('instrumentMode', 'IW'))
                .filterDate(year + '-01-01', year + '-12-31')
                .filterBounds(roi)
                .filter(ee.Filter.listContains('transmitterReceiverPolarisation', polarisation))
                .select(polarisation)
                .filter(ee.Filter.eq('orbitProperties_pass', orbit_direction));

```