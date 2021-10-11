# EO-Toolbox

EO-Toolbox is a set of **Jupyter Notebooks** that explains in detail the different steps to process Sentinel-2 images using `Python 3.6`

1. Download Sentinel images with `sentinelsat`
1. Pre-processing Sentinel-2 images
3. Deriving biophysical Indicators (e.g. NDVI, NDWI,...)
4. Designing srategies to split in-situ data into a calibration and a validation datasets
5. Creating classification with Random Forest


## Jupyter Notebooks

#### Downloading Sentinel images

[Download Sentinel images](https://nicolasdeffense.github.io/eo-toolbox/notebooks/download_images.html)


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


# Installation

## Launch Jupyter-Lab from your personal computer

! Requires sotckage to install mMiniconda (or Anaconda) and the necessary packages !

1. Download Miniconda (or Anaconda)

I recommend to use the `conda` package manager to install all the requirements. You can install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or install the (larger) [Anaconda](https://www.anaconda.com/products/individual) distribution.

`conda` is a powerful package manager and environment manager that you use with command line commands at the Anaconda Prompt for Windows, or in a terminal window for macOS or Linux.

--> [Getting started with conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html)

You can also check the [conda cheat sheet](cheat_sheets/conda_cheat_sheet.pdf) to get an overview of all commands.

1. Download the YAML file `env_lbrat2104.yml` from Git to your computer.

2. Create a conda envrionment from YAML file
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


3. Activate environment
```sh
conda activate lbrat2104
```

4. Download other libaries

Some libraries can not be installed with `conda` and must be isntalled through `pip`

For instance, to install [sentinelsat](https://sentinelsat.readthedocs.io/en/stable/index.html) you must launch this command :

```sh
pip install sentinelsat
```

5. Test the environment (optional)

To make sure everything was installed correctly, open a terminal, and change its directory (cd) so that your working directory is repository you dowloaded. Then enter the following:
```sh
python3 check_environment.py
```

6. Launch Jupyter-Lab
```sh
jupyter lab
```


## Launch Jupyter-Lab from computer room

1. Open *Command Prompt* (Windows) or *Terminal* (MacOS)

2. Navigate to the disk where the environment was created
```sh
X:
```

3. Activate environment
```sh
conda activate lbrat2104
```

4. Launch Jupyter-Lab
```sh
jupyter lab
```

5. Close jupyter notebook  
`CTRL-C`  
`CTRL-C`  


## Launch Jupyter-Lab from lab server

1. Connect to Windows server GEO-14 (*geo14.elie.ucl.ac.be*)

*Don't forget to activate your VPN if you're not connected in eduroam WIFI !*

2. Open *Anaconda Prompt (Anaconda3)*

3. Activate **LBRAT2104**'s environment
```sh
conda activate lbrat2104
```
*The name of the environment must appear before the name of the disk*  
`(lbrat2104) C:\>`

4. Move to home disk, the disk where you stored all you data
```sh
H:
```

5. Launch Jupyter-Lab
```sh
jupyter lab
```
*By default, Jupyter Lab opens in Internet Explorer and this does not work. You need to copy the URL link and paste it into Google Chrome instead.*

6. Navigates to the folder where the notebooks are located

*You can download all the content of this git by clicking on "Code>Download ZIP".*


***

*This repository was created in the framework of the course **LBRAT2104 - Land Monitoring by Advanced Earth Observation** by Nicolas Deffense.*