---
layout: sub_page
title: Validation
---

<a href="https://nicolasdeffense.github.io/eo-toolbox/notebooks/7_Classification/validation.html"> <i class="fas fa-eye fa-lg"></i></a>
<a href="https://nicolasdeffense.github.io/eo-toolbox/notebooks/7_Classification/validation.ipynb"> <i class="fas fa-download fa-lg"></i></a>


When a classification is performed, whether it is generated with machine learning tools such as Random Forest or based on thresholds of a spectral index for example, it should be validated on the basis of *in situ* data (ground data). In the case where *in situ* data are also used to generate the classification, the data used to validate the classification must be independent.

The validation data are used to assess the map accuracy defined by the agreement between the map output and the validation data assumed to be the truth. The most common way to derive the map accuracy is to analyse the confusion matrix, which is a square co-occurrence matrix compiling the number of samples matching a given land cover class with validation information. Diagonal values represent the agreement frequency between the validation data and the map output, while non-diagonal values represent the errors.

{% include_relative NAMUR_2020_CM.html} 

cat(plotly:::plotly_iframe())

<iframe width=100%, height=650, src='NAMUR_2020_CM.html'></iframe>

<iframe src="NAMUR_2020_CM.html" width="100%" height="400" id="igraph" scrolling="no" seamless="seamless" frameBorder="0"> </iframe>


Among fourteen class-level and twenty map-level accuracy metrics, Liu et al. (2007) recommended user accuracy (UA), producer accuracy (PA) and overall accuracy (OA) as primary accuracy measures. For binary maps such as the cropland mask, the OA depends to a large extent on the respective proportion of both classes in the validation data set. In this case, the F-Score, the use of which has been recently adopted, is a more informative accuracy metric.


The **Overall Accuracy** (OA) is computed as the ratio of the number of all correctly classified samples to the total number (N) of all validation samples. A standard target for the overall accuracy of a land cover map is typically 85 percent. In some cases, simple land cover maps that include very few classes can reach 90 percent.


<figure class="image">
<img src="https://latex.codecogs.com/svg.latex? \mathrm{OA}(\%)=\left(100 \times \sum_{k=1}^{q} n_{\mathrm{kk}}\right) / \mathrm{N}"/>
</figure>

The **User Accuracy** (UA) for a given land cover class i is the ratio between the number of correctly classified samples as belonging to this class and all samples classified in this class.

<figure class="image">
<img src="https://latex.codecogs.com/svg.latex? \mathrm{UA}_{\mathrm{i}}(\%)=100 \times \frac{n_{i i}}{n_{i+}}"/>
</figure>

The **Producer Accuracy** (PA) for a given class i is the ratio between the number of correctly classified samples and all samples belonging to this class, according to the validation data.

<figure class="image">
<img src="https://latex.codecogs.com/svg.latex? \mathrm{PA}_{\mathrm{i}}(\%)=100 \times \frac{n_{i i}}{n_{+i}}"/>
</figure>

The **F-score** is calculated as a combination of PA and UA for a given land cover class i:

<figure class="image">
<img src="https://latex.codecogs.com/svg.latex? \mathrm{F-score}_{\mathrm{i}}(\%)=\frac{2 \times \mathrm{PA}_{\mathrm{i}} \times \mathrm{UA}_{\mathrm{i}}}{\mathrm{PA}_{\mathrm{i}} + \mathrm{UA}_{\mathrm{i}}} "/>
</figure>

---

[Handbook on remote sensing for agricultural statistics](https://www.researchgate.net/publication/319876837_Handbook_on_remote_sensing_for_agricultural_statistics)