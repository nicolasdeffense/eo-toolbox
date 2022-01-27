

# Remove the last row of pixels (below the raster) that is badly cut by the ROI
# (also works if it is the last column of pixels)
# ! Does not work if it is the first row or column (due to the transform parameter that is difficult to change)

#out_image = out_image[0,:-1,]
#out_image = np.expand_dims(out_image, axis=0)