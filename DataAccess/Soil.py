from osgeo import gdal
import pandas as pd

"""Takes longitudinal and latitudinal coords and returns the location of the pixels they correspond to in the raster 
file"""


def coordsToPixels(long, lat, rows, cols):
    long_max = 180
    long_min = -180
    lat_max = 90
    lat_min = -90
    assert long_min <= long <= long_max and lat_min <= lat <= lat_max
    lat_idx = int((lat - lat_min) / (lat_max - lat_min) * rows)
    long_idx = int((long - long_min) / (long_max - long_min) * cols)
    return long_idx, lat_idx


"""incomplete currently just displays some generic data about raster files"""


def getSoilData(long, lat, detailed):
    # finds coordinates from raster file
    raster = gdal.Open("WISE30sec/Interchangeable_format/wise_30sec_v1.tif")
    rows = raster.RasterYSize
    cols = raster.RasterXSize
    # prints dimensions of raster file
    print(cols, rows)
    band = raster.GetRasterBand(1)
    data = band.ReadAsArray(0, 0, cols, rows)
    # prints the values of pixels near the start and end of raster file
    print(data)

    # opens a .tsv file that can be used to gather some metadata about the raster file
    df = pd.read_csv('WISE30sec/Interchangeable_format/wise_30sec_v1.tsv', sep='\t')
    print(df)

    # finds the map code associated with the pixel
    x, y = coordsToPixels(long, lat, rows, cols)
    print(data[y][x])
    pixel = df.loc[df["pixel_vaue"] == data[y][x]]
    print(pixel)
    map_code = pixel.get("description")

    # finds the profile ID of the corresponding map code
    df1 = pd.read_csv('WISE30sec/Interchangeable_format/HW30s_MapUnit.txt', sep=',', dtype=str)
    print(df1)
    print(str(map_code)[7:17])
    soil_record = df1.loc[df1["NEWSUID"] == str(map_code)[7:17]]
    profile_id = soil_record.get()


getSoilData(0, 0, 1)
