---
layout: sub_page
title: Vector data
---

<a href="https://nicolasdeffense.github.io/eo-toolbox/notebooks/3_In_situ_data/in_situ_data.html"> <i class="fas fa-eye fa-lg"></i></a>
<a href="https://nicolasdeffense.github.io/eo-toolbox/notebooks/3_In_situ_data/in_situ_data.ipynb"> <i class="fas fa-download fa-lg"></i></a>


In addition to satellite EO imagery or time series, land cover / crop type mapping relies on *in situ* vector data collection to :
- train the classification algorithm a priori (or to label the output classes a posteriori in the case of unsupervised classification algorithms)
- validate the output (assess map quality)


The validation data set is necessarily a high-quality reference data set, to be used as so-called ground-truth to assess the accuracy of a classification map. **Validation should never be confused with the intercomparison of maps; this process quantifies the discrepancies between the maps, but cannot rigorously attribute errors to one or the other.**

Field data collection is a resource-intensive and time-consuming activity, particularly if it is sought to cover large areas. While sampling theory should define the design, logistic and resource constraints impel identification of the optimal trade-off in terms of performance and cost-efficiency.

Training data sets and validation data sets may also be collected by on-screen delineation based on visual and interactive interpretation of multispectral colour composites. Very high spatial resolution (VHR) images made available on line by Google Earth, Bing, and similar geoportals, are often used for digitizing polygons instead of ground data. The acquisition date of these images displayed on geoportals can be very diverse and does not necessarily correspond to any given year of observation. This is therefore quite efficient for the most stable land cover types but should not be used for crop type for instance as they might change annually.

---

[Handbook on remote sensing for agricultural statistics](https://nicolasdeffense.github.io/eo-toolbox/docs/Remote_Sensing_for_Agricultural_Statistics.pdf)

[JECAM Guidelines for Field Data Collection](https://nicolasdeffense.github.io/eo-toolbox/docs/JECAM_Guidelines_for_Field_Data_Collection_v1_0.pdf)