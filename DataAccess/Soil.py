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
    pixels = pd.read_csv('WISE30sec/Interchangeable_format/wise_30sec_v1.tsv', sep='\t')
    print(pixels)

    # finds the map code associated with the pixel
    x, y = coordsToPixels(long, lat, rows, cols)
    print(data[y][x])
    pixel_value = pixels.loc[pixels["pixel_vaue"] == data[y][x]]
    print(pixel_value)
    map_code = str(pixel_value.get("description"))[7:17]

    # finds the profile ID of the corresponding map code
    map_units = pd.read_csv('WISE30sec/Interchangeable_format/HW30s_MapUnit.txt', sep=',', dtype=str)
    print(map_units)
    print(map_code)
    soil_record = map_units.loc[map_units["NEWSUID"] == map_code]
    print(soil_record)
    no_profiles = int(soil_record.get("NoSoilComp").iloc[0])
    print(no_profiles)
    profiles = {}
    soil_map_unit = str(soil_record.get("SoilMapUnit"))[8:-32]
    soil_climate_code = soil_map_unit[no_profiles*4:no_profiles*4+2]
    print(soil_climate_code)
    print(soil_map_unit)
    if detailed == 1:
        for i in range(no_profiles):
            #profiles[soil_record.get]
            pass
    else:
        dom_profile = str(soil_record.get("DomFAO_Name"))[8:10]
        dom_prop = int(str(soil_record.get("DomFAO_Prop"))[7:10])
        readProfile(soil_climate_code)

        print(dom_profile)
        print(dom_prop)



#def readProfile(profile, )

getSoilData(0, 0, 0)