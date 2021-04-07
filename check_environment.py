#!/usr/bin/python3

import importlib

packages = ['numpy',
            'pandas',
            'geopandas',
            'matplotlib',
            'rasterio',
            'rasterstats',
            'scipy',
            'sklearn']

bad = []
for package in packages:
    try:
        importlib.import_module(package)
    except ImportError:
        bad.append(f"Can't import {package}")
else:
    if len(bad) > 0:
        print('Your tutorial environment is not yet fully set up:')
        print('\n'.join(bad))
    else:
        try:
            import pandas
            import geopandas
            print("All good. Enjoy the EO-Toolbox !")
        except Exception as e:
            print("Couldn't read builtin data.")
            print(e)