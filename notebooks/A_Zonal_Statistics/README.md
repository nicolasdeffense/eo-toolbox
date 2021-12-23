# Zonal Statistics

`rasterstats` is a Python module for summarizing geospatial raster datasets based on vector geometries.

Geospatial data typically comes in one of two data models:
- *rasters* which are similar to images with a regular grid of pixels whose values represent some spatial phenomenon (e.g. elevation)
- *vectors* which are entities with discrete geometries (e.g. state boundaries).

`rasterstats` exists solely to extract information from geospatial raster data based on vector geometries.

This involves zonal statistics: a method of summarizing and aggregating the raster values intersecting a vector geometry. For example, zonal statistics provides answers such as the mean precipitation or maximum elevation of an administrative unit.

By default, the **zonal_stats** function will return the following statistics

- min
- max
- mean
- count

Optionally, these statistics are also available.

- sum
- std
- median
- majority
- minority
- unique
- range
- nodata
- percentile (see note below for details)


[> See User Manual](https://pythonhosted.org/rasterstats/manual.html)

## Coninuous values

If you are interested of NDVI mean by polygon for each date of a timeserie for instance.

[> Notebook Zonal Stats for continuous values](https://nicolasdeffense.github.io/eo-toolbox/notebooks/A_Zonal_Statistics/zonal_stats_continuous.html)

## Categorical values

You can treat rasters as categorical (i.e. raster values represent discrete classes) if you’re only interested in the counts of unique pixel values.

> For example, you may have a crop type raster and want to summarize number of pixels of each classes by polygon. Statistics such as mean, median, sum, etc. don’t make much sense in this context (What’s the sum of urban + grassland?).

[> Notebook Zonal Stats for categorical values](https://nicolasdeffense.github.io/eo-toolbox/notebooks/A_Zonal_Statistics/zonal_stats_categorical.html)