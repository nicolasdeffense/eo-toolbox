---
layout: sub_page
title: Composites
---

<a href="https://nicolasdeffense.github.io/eo-toolbox/notebooks/D_Composites/composites.html"> <i class="fas fa-eye fa-lg"></i></a>
<a href="https://nicolasdeffense.github.io/eo-toolbox/notebooks/D_Composites/composites.ipynb"> <i class="fas fa-download fa-lg"></i></a>


Individual remote sensing images can be affected by noisy data, including clouds, cloud shadows, and haze. To produce cleaner images that can be compared more easily across time, we can create “summary” images or “composites” that combine multiple images into one.

Some methods for generating composites include estimating the `median`, `mean`, `minimum`, or `maximum` pixel values in an image. Care must be taken with these, as they do not necessarily preserve spectral relationships across bands

## Median composites

One of the key reasons for generating a composite is to replace pixels classified as clouds with realistic values from the available data. This results in an image that doesn’t contain any clouds. In the case of a median composite, each pixel is selected to have the median (or middle) value out of all possible values.

>Care should be taken when using these composites for analysis, since the relationships between spectral bands are not preserved. These composites are also affected by the timespan they’re generated over. For example, the median pixel in a single season may be different to the median value for the whole year.

## Mean composites

Mean composites involve taking the average value for each pixel, rather than the middle value as is done for a median composite. Unlike the median, the mean composite can contain pixel values that were not part of the original dataset.

>Care should be taken when interpreting these images, as extreme values (such as unmasked cloud) can strongly affect the mean.

## Minimum and maximum composites

These composites can be useful for identifying extreme behaviour in a collection of satellite images.

For example, comparing the maximum and minimum composites for a given band index could help identify areas that take on a wide range of values, which may indicate areas that have high variability over the time-line of the composite.

## Nearest-time composites (not implemented yet !)

To get an image at a certain time, often there is missing data, due to clouds and other masking. We can fill in these gaps by using data from surrounding times.

### Most-recent composite

Sometime we may want to determine what the landscape looks like by examining the most recent image. If we look at the last image for our dataset, we may see there is some missing data in the last image.

### Before and after composites

Often it is useful to view images before and after an event, to see the change that has occured. To generate a composite on either side of an event, we can split the dataset along time.

### Nearest time composite

Sometimes we just want the closest available data to a particular point in time. This composite will take values from before or after the specified time to find the nearest observation.

---


[Generating composites images with Digital Earth](https://docs.digitalearthafrica.org/fr/latest/sandbox/notebooks/Frequently_used_code/Generating_composites.html)