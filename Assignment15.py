# Team Nikoula: Latifah & Nikos
# Date: 26/1/2015

# import the requirements
import os
from osgeo import gdal
from osgeo.gdalconst import GA_ReadOnly, GDT_Float32
import numpy as np

os.getcwd() # working directory

# Open Landsat satellite images
driver = gdal.GetDriverByName('GTiff')

band4 = gdal.Open('Python/bandname4.tif)
band5 = gdal.Open('Python/bandname5.tif)

# Reading band's per array and chanding the store type into float
band4 = band4.GetRasterBand(1)
band5 = band5.GetRasterBand(1)
band4Arr = band4.ReadAsArray(0, 0, band4.RasterXSize, band4.RasterYSize)
band5Arr = band5.ReadAsArray(0, 0, band5.RasterXSize, band5.RasterYSize)
band4Arr = band4Arr.astype(np.float32)
band5Arr = band5Arr.astype(np.float32)

# Create the mask layer
mask = np.greater(band4Arr+band5Arr, 0)

# Calculate NDWI
ndwi = np.choose(mask,(-99,(band4Arr-band5Arr)/(band4Arr+band5Arr)))
print "NDWI min and max values", ndwi.min(), ndwi.max()

# Create an image as an output
outDataSet = driver.Create('Python/NDWI.tif', band4.RasterXSize, band4.RasterYSize, 1, GDT_Float32)
outBand = outDataSet.GetRasterBand(1)
outBand.WriteArray(ndwi, 0, 0)
outBand.SetNoDataValue(-99)
outBand.FlushCache()
outDataSet.FlushCache()
                  #END
