---
layout: sub_page
title: Spectral indices
---

[<img src="./buttons/view_button.png" width="100"/>](https://nicolasdeffense.github.io/eo-toolbox/notebooks/6_Spectral_indices/spectral_indices.html)

[<img src="./buttons/download_button.png" width="100"/>](https://nicolasdeffense.github.io/eo-toolbox/notebooks/6_Spectral_indices/spectral_indices.ipynb)


## NDVI - Normalized Difference Vegetation Index

NDVI is used to outline the presence of vegetation. It is used to indicate relative density, or the amount, of the green vegetation present in the image. This index uses reflectance from a red band around 0.66 μm and a near-Infrared band around 0.86 μm. The red band is found in the absorption region of the chlorophyll, while the near-IR band is used in high reflectance plateau of the vegetation canopies. These two bands sense different depths over the vegetation canopies.


<img src="https://latex.codecogs.com/svg.latex?NDVI = \frac{NIR - RED}{NIR + RED} = \frac{B08 - B04}{B08 + B04}" title="NDVI = \frac{NIR - RED}{NIR + RED} = \frac{B08 - B04}{B08 + B04}"/>


## NDWI - Normalized Difference Water Index

NDWI concept as formulated by Gao combining reflectance of NIR and SWIR has a wide range of application. It can be used for exploring water content at single leaf level as well as canopy/satellite level. The range of application of NDWI spreads from agricultural monitoring for crop irrigation and pasture management to forest monitoring for assessing fire risk and live fuel moisture particularly relevant in the context of climate change.

<img src="https://latex.codecogs.com/svg.latex? NDWI = \frac{NIR - SWIR}{NIR + SWIR} = \frac{B08 - B11}{B08 + B11}"/>

## NDSI - Normalized Difference Snow Index

NDSI is used to delineate the presence of snow/ice. It is a standardized ratio of the difference in the reflectance in the bands that take advantage of unique signature and the spectral difference to indicate snow from the surrounding features and even clouds.

<img src="https://latex.codecogs.com/svg.latex? NDSI = \frac{GREEN - SWIR}{GREEN + SWIR} = \frac{B03 - B11}{B03 + B11}"/>


## NBR - Normalized Burn Ratio

To detect burned areas, the NBR index is the most appropriate choice. Using bands 8 and 12 it highlights burnt areas in large fire zones greater than 500 acres. To observe burn severity, you may subtract the post-fire NBR image from the pre-fire NBR image.

The NIR and SWIR parts of the electromagnetic spectrum are a powerful combination of bands to use for this index given vegetation reflects strongly in the NIR region of the electromagnetic spectrum and weekly in the SWIR. Alternatively, it has been shown that a fire scar which contains scarred woody vegetation and earth will reflect more strongly in the SWIR part of the electromagnetic spectrum and beyond (see figure below).

<img src="https://latex.codecogs.com/svg.latex? NBR = \frac{NIR - SWIR}{NIR + SWIR} = \frac{B08 - B12}{B08 + B12}"/>


For a given area, NBR is calculated from an image just prior to the burn and a second NBR is calculated for an image immediately following the burn. Burn extent and severity is judged by taking the difference between these two index layers:

<img src="https://latex.codecogs.com/svg.latex? dNBR = NBR_{prefire} - NBR_{postfire}"/>


## BAIS2 - Burned Area Index for Sentinel-2

BAIS2 adapts the traditional BAI for Sentinel-2 bands, taking advantage of the wider spectrum of Visible, Red-Edge, NIR and SWIR bands.

Values description: The range of values for the BAIS2 is -1 to 1 for burn scars, and 1 - 6 for active fires. Different fire intensities may result in different thresholds, the current values were calibrates, as per original author, on mostly Mediterranen regions.

<img src="https://latex.codecogs.com/svg.latex? BAIS2 = \left(1-\sqrt{\frac{B06*B07*B8A}{B4}}\right) *\left(\frac{B12-B8A}{\sqrt{B12+B8A}}+1\right)"/>

## BRIGHTNESS

Brightness provide complementary information improving the discrimination between crop and no-crop areas.

<img src="https://latex.codecogs.com/svg.latex? Brightness = \sqrt{GREEN^{2}+RED^{2}+NIR^{2}+SWIR^{2}} = \sqrt{B03^{2}+B04^{2}+B08^{2}+B11^{2}}"/>

## SWI - Surface Waterproofing Index

SWI, based on NDVI and NDWI, is a useful tool for monitoring waterproofing.

<img src="https://latex.codecogs.com/svg.latex? SWI = (NDVI - NDWI)^2"/>





[> Notebook to compute difference between spectral indices](https://nicolasdeffense.github.io/eo-toolbox/notebooks/6_Spectral_indices/spectral_indices_difference.html)


[Source](https://eos.com/make-an-analysis/index-stack/)