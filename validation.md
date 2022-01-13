---
layout: sub_page
title: Validation
---

[<img src="./buttons/view_button.png" width="100"/>](https://nicolasdeffense.github.io/eo-toolbox/notebooks/7_Classification/validation.html)

[<img src="./buttons/download_button.png" width="100"/>](https://nicolasdeffense.github.io/eo-toolbox/notebooks/7_Classification/validation.ipynb)

The validation data are used to assess the map accuracy defined by the agreement between the map output and the validation data assumed to be the truth. The most common way to derive the map accuracy is to analyse the confusion matrix, which is a square co-occurrence matrix compiling the number of samples matching a given land cover class with validation information. Diagonal values represent the agreement frequency between the validation data and the map output, while non-diagonal values represent the errors.

Among fourteen class-level and twenty map-level accuracy metrics, Liu et al. (2007) recommended user accuracy (UA), producer accuracy (PA) and overall accuracy (OA) as primary accuracy measures. For binary maps such as the cropland mask, the OA depends to a large extent on the respective proportion of both classes in the validation data set. In this case, the F-Score, the use of which has been recently adopted, is a more informative accuracy metric.


The OA is computed as the ratio of the number of all correctly classified samples to the total number (N) of all validation samples. A standard target for the overall accuracy of a land cover map is typically 85 percent. In some cases, simple land cover maps that include very few classes can reach 90 percent.

OA(%)=(100x " 𝑛𝑛kk)/N

<img src="https://latex.codecogs.com/svg.latex? \mathrm{OA}(\%)=\left(100 \times \sum_{k=1}^{q} n_{\mathrm{kk}}\right) / \mathrm{N}"/>


The UA for a given land cover class i is the ratio between the number of correctly classified samples as belonging to this class and all samples classified in this class.

<img src="https://latex.codecogs.com/svg.latex? \mathrm{UA}_{\mathrm{i}}(\%)=100 \times \frac{n_{i i}}{n_{i+}}"/>


The PA for a given class i is the ratio between the number of correctly classified samples and all samples belonging to this class, according to the validation data.

<img src="https://latex.codecogs.com/svg.latex? \mathrm{PA}_{\mathrm{i}}(\%)=100 \times \frac{n_{i i}}{n_{+i}}"/>

The F-score is calculated as a combination of PA and UA for a given land cover class i:

<img src="https://latex.codecogs.com/svg.latex? \mathrm{F-score}_{\mathrm{i}}(\%)=\frac{2 \times \mathrm{PA}_{\mathrm{i}} \times \mathrm{UA}_{\mathrm{i}}}{\mathrm{PA}_{\mathrm{i}} + \mathrm{UA}_{\mathrm{i}}} "/>

---

[Handbook on remote sensing for agricultural statistics](https://www.researchgate.net/publication/319876837_Handbook_on_remote_sensing_for_agricultural_statistics)