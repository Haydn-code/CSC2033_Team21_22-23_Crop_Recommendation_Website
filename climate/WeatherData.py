from osgeo import gdal
import numpy as np
from DataAccess.Soil import coordsToPixels

def getWeatherData(long, lat, folder):
    weather_dict = {
        'prec': [],
        'srad': [],
        'temp_avg': [],
        'temp_max': [],
        'temp_min': [],
        'wind': []
    }

    # gets the size of the raster file
    temp_file = f"{folder}/prec/prec_01.tif"
    ds = gdal.Open(temp_file)
    rows = ds.RasterYSize
    cols = ds.RasterXSize

    # gets the pixel coordinates
    x, y = coordsToPixels(long, lat, rows, cols)

    # loops through the folders and files, and extracts data
    for category in weather_dict.keys():
        for month in range(1, 13):
            # Construct the filename and open the file with GDAL
            filename = f"{folder}/{category}/{category}_{month:02d}.tif"
            ds = gdal.Open(filename)

            # Get the pixel value at the given coordinates
            band = ds.GetRasterBand(1)
            value = band.ReadAsArray(x, y, 1, 1)[0][0]

            # Add the value to the data dictionary
            weather_dict[category].append(value)

    return weather_dict
