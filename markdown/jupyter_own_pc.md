---
layout: sub_page
title: Jupyter Lab
description: How to access JupyterLab on your own PC/Mac?
---

> ! Requires stockage to install Miniconda (or Anaconda) and the necessary packages !

1. Download Miniconda (or Anaconda)  

    I recommend to use the `conda` package manager to install all the requirements. You can install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or install the (larger) [Anaconda](https://www.anaconda.com/products/individual) distribution.

    > `conda` is a powerful package manager and environment manager that you use with command line commands at the Anaconda Prompt for Windows, or in a terminal window for macOS or Linux.

    [Getting started with conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html)

    You can also check the [conda cheat sheet](../cheat_sheets/conda_cheat_sheet.pdf) to get an overview of all commands.

2. Download the YAML file [env_lbrat2104.yml](../installation/env_lbrat2104.yml)

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

    To make sure everything was installed correctly you can run the small python script [check_environment.py](../installation/check_environment.py)

    ```sh
    python3 check_environment.py
    ```

8. Launch Jupyter-Lab
    ```sh
    jupyter lab
    ```