# EO-Toolbox

EO-Toolbox is a set of Jupyter Notebooks that explains in detail the different steps to process Sentinel-2 images using `Python 3.6`

1. Pre-processing Sentinel-2 images
3. Deriving biophysical Indicators (e.g. NDVI, NDWI,...)
4. Designing srategies to split in-situ data into a calibration and a validation datasets
5. Creating classification with Random Forest



## Jupyter Notebooks

#### Vector data

[Build region of Interest](https://nicolasdeffense.github.io/eo-toolbox/notebooks/region_of_interest.html)

[In-Situ data](https://nicolasdeffense.github.io/eo-toolbox/notebooks/in_situ.html)


#### Pre-processing Sentinel-2 data

[Preprocess Sentinel-2 data](https://nicolasdeffense.github.io/eo-toolbox/notebooks/sentinel_2_prepro.html)

[Compute Spectral Indices](https://nicolasdeffense.github.io/eo-toolbox/notebooks/spectral_indices.html)

[Extract statistics from timeserie](https://nicolasdeffense.github.io/eo-toolbox/notebooks/extract_stats_timeserie.html)


#### Classification

[In-Situ sampling design](https://nicolasdeffense.github.io/eo-toolbox/notebooks/in_situ_sampling_design.html)

[Random Forest Classification](https://nicolasdeffense.github.io/eo-toolbox/notebooks/random_forest_classification.html)

[Validation](https://nicolasdeffense.github.io/eo-toolbox/notebooks/validation.html)


#### Tools

[Build multi-band images and RGB composite](https://nicolasdeffense.github.io/eo-toolbox/notebooks/multiband_raster.html)

[Compute Zonal Statistics](https://nicolasdeffense.github.io/eo-toolbox/notebooks/zonal_stats.html)

[Create graphs with matplotlib](https://nicolasdeffense.github.io/eo-toolbox/notebooks/graphics.html)


## Installation notes

To use the notebooks, you should first install :

- [Python 3.6](https://www.python.org)
- [Jupyter Notebook](http://jupyter.org)

and then the following python packages/libraries :

- [numpy 1.19.2](https://numpy.org)
- [pandas 1.1.5](https://pandas.pydata.org)
- [geopandas 0.8.1](https://geopandas.org/)
- [matplotlib 3.3.4](https://matplotlib.org)
- [rasterio 1.1.0](https://rasterio.readthedocs.io/en/latest/intro.html)
- [rasterstats 0.14.0](https://pythonhosted.org/rasterstats/)
- [scipy 1.5.2](https://www.scipy.org/about.html)
- [scikit-learn 0.24.1](https://scikit-learn.org/stable/)
- [sentinelsat 1.0.1](https://sentinelsat.readthedocs.io/en/stable/index.html)


If you do not yet have these packages/libraries installed, I recommend to use the conda package manager to install all the requirements. You can install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or install the (larger) [Anaconda](https://www.anaconda.com/products/individual) distribution.



### Test the environment

To make sure everything was installed correctly, open a terminal, and change its directory (cd) so that your working directory is repository you dowloaded. Then enter the following:

```sh
python3 check_environment.py
```


*This repository was created in the framework of the course **LBRAT2104 - Land Monitoring by Advanced Earth Observation** by Nicolas Deffense.*