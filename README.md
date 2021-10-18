# EO-Toolbox

EO-Toolbox is a set of **Jupyter Notebooks** that explains in detail the different steps to process Sentinel-2 images using `Python 3.6`

This repository was created in the framework of the course [LBRAT2104 - Land Monitoring by Advanced Earth Observation](https://uclouvain.be/cours-2021-lbrat2104) by Nicolas Deffense.


# Jupyter Notebooks

## Downloading Sentinel images

[Download Sentinel images](https://nicolasdeffense.github.io/eo-toolbox/notebooks/html/download_images.html)

## Vector data

[Build region of Interest](https://nicolasdeffense.github.io/eo-toolbox/notebooks/html/region_of_interest.html)

[In-Situ data](https://nicolasdeffense.github.io/eo-toolbox/notebooks/html/in_situ.html)

## Pre-processing Sentinel-2 data

[Preprocess Sentinel-2 data](https://nicolasdeffense.github.io/eo-toolbox/notebooks/html/sentinel_2_prepro.html)

[Compute Spectral Indices (NDVI, NDWI, ...)](https://nicolasdeffense.github.io/eo-toolbox/notebooks/html/spectral_indices.html)

[Extract statistics from timeserie](https://nicolasdeffense.github.io/eo-toolbox/notebooks/html/extract_stats_timeserie.html)

## Classification

[In-Situ sampling design](https://nicolasdeffense.github.io/eo-toolbox/notebooks/html/in_situ_sampling_design.html)

[Random Forest Classification](https://nicolasdeffense.github.io/eo-toolbox/notebooks/html/random_forest_classification.html)

[Validation](https://nicolasdeffense.github.io/eo-toolbox/notebooks/html/validation.html)

## Tools

[Build multi-band images and RGB composite](https://nicolasdeffense.github.io/eo-toolbox/notebooks/html/multiband_raster.html)

[Compute Zonal Statistics](https://nicolasdeffense.github.io/eo-toolbox/notebooks/html/zonal_stats.html)

[Create graphs with matplotlib](https://nicolasdeffense.github.io/eo-toolbox/notebooks/html/graphics.html)

[Count frequency](https://nicolasdeffense.github.io/eo-toolbox/notebooks/html/count_frequency_pixels.html)


# Installation

## Launch Jupyter-Lab from your personal computer

> ! Requires stockage to install Miniconda (or Anaconda) and the necessary packages !

1. Download Miniconda (or Anaconda)  

I recommend to use the `conda` package manager to install all the requirements. You can install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or install the (larger) [Anaconda](https://www.anaconda.com/products/individual) distribution.

> `conda` is a powerful package manager and environment manager that you use with command line commands at the Anaconda Prompt for Windows, or in a terminal window for macOS or Linux.

[Getting started with conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html)

You can also check the [conda cheat sheet](cheat_sheets/conda_cheat_sheet.pdf) to get an overview of all commands.

2. Download the YAML file [env_lbrat2104.yml](installation/env_lbrat2104.yml)

3. Open *Anaconda Prompt* (Windows) or *Terminal* (MacOS)

4. Create a conda envrionment from YAML file
```sh
conda env create --file env_lbrat2104.yml
```

The following python packages/libraries are now installed :
- [numpy 1.19.2](https://numpy.org)
- [pandas 1.1.5](https://pandas.pydata.org)
- [geopandas 0.8.1](https://geopandas.org/)
- [matplotlib 3.3.4](https://matplotlib.org)
- [rasterio 1.1.0](https://rasterio.readthedocs.io/en/latest/intro.html)
- [rasterstats 0.14.0](https://pythonhosted.org/rasterstats/)
- [scipy 1.5.2](https://www.scipy.org/about.html)
- [scikit-learn 0.24.1](https://scikit-learn.org/stable/)
- [jupyter lab](http://jupyter.org)


5. Activate **LBRAT2104**'s environment
```sh
conda activate lbrat2104
```

6. Download other libaries with `pip`

> Some libraries can not be installed with `conda` and must be installed through `pip`

For instance, to install [sentinelsat](https://sentinelsat.readthedocs.io/en/stable/index.html) you must launch this command :

```sh
pip install sentinelsat
```

7. Test the environment (optional)

To make sure everything was installed correctly you can run the small python script [check_environment.py](installation/check_environment.py)
```sh
python3 check_environment.py
```

8. Launch Jupyter-Lab
```sh
jupyter lab
```


## Launch Jupyter-Lab from computer room

*TODO: check if everything is ok*

1. Open *Anaconda Prompt*

2. Navigate to the disk where the environment was created
```sh
X:
```

3. Activate **LBRAT2104**'s environment
```sh
conda activate /anaconda_env/LBRAT2104_env_ndeffense
```

4. Launch Jupyter-Lab
```sh
jupyter lab
```

5. Close Jupyter-Lab  
`CTRL-C`  
`CTRL-C`  


## Launch Jupyter-Lab from Geo14

1. Connect to Windows server Geo14 (*geo14.elie.ucl.ac.be*)

> Only available to students doing their master thesis with Pierre Defourny  
> *Don't forget to activate your VPN if you're not connected in eduroam WIFI !*

2. Open *Anaconda Prompt*

3. Activate **LBRAT2104**'s environment
```sh
conda activate G:\conda_env\lbrat2104
```
*The name of the environment must appear before the name of the disk*  
`(G:\conda_env\lbrat2104) C:\>`

4. Move to home disk, the disk where you stored all you data
```sh
H:
```

5. Launch Jupyter-Lab
```sh
jupyter lab
```
> By default, Jupyter Lab opens in Internet Explorer and this does not work. You need to copy the URL link and paste it into Google Chrome instead.

6. Navigates to the folder where the notebooks are located

> You can download all the content of this git by clicking on "Code>Download ZIP".


# TODO's

- add temporal filtering (e.g. linear interpolation)
- add Google Earth link QGIS in slide
- colormap classification via script de Quentin