from osgeo import gdal
import pandas as pd


"""Takes longitudinal and latitudinal coords and returns the location of the pixels they correspond to in the raster 
file"""
def coordsToPixels(long, lat):
    assert -180 <= long <= 180 and -90 <= lat <= 90
    lat_idx = int((lat - -90) / (90 - -90) * 16753)
    long_idx = int((long - -180) / (180 - -180) * 43201)
    return long_idx, lat_idx


print(coordsToPixels(0, -90))


"""incomplete currently just displays some generic data about raster files"""
def getSoilData(long, lat):
    assert -180 <= long <= 180 and -90 <= lat <= 90
    # finds coordinates from raster file
    raster = gdal.Open("WISE30sec/Interchangeable_format/wise_30sec_v1.tif")
    rows = raster.RasterXSize
    cols = raster.RasterYSize
    # prints dimensions of raster file
    print(rows)
    print(cols)
    band = raster.GetRasterBand(1)
    data = band.ReadAsArray(0, 0, rows, cols)
    # prints the values of pixels near the start and end of raster file
    print(data)

    # opens a .tsv file that can be used to gather some metadata about the raster file
    df = pd.read_csv('WISE30sec/Interchangeable_format/wise_30sec_v1.tsv', sep='\t')
    print(df)

getSoilData(0,0)