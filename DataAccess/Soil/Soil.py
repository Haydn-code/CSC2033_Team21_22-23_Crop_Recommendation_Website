from osgeo import gdal
import pandas as pd

"""Takes longitudinal and latitudinal coords and returns the location of the pixels they correspond to in a raster 
file

Parameters:
long (float): longitudinal coords
lat (float): latitudinal coords
cols (int): the number of columns of pixels in the raster file
rows (int): the number of rows of pixels in the raster file

Returns:
long_idx (int) the idx of the column of the pixel
lat_idx (int) the idx of the row of the pixel

Errors: displays an assertion error if the lat isn't between 90 and -90 or if long isn't between 180 and -180"""


def coordsToPixels(long, lat, rows, cols):
    long_max = 180
    long_min = -180
    lat_max = 90
    lat_min = -90
    assert long_min <= long < long_max and lat_min <= lat < lat_max
    # converts the coords to their grid reference in the raster file
    lat_idx = rows - int((lat - lat_min) / (lat_max - lat_min) * rows) - 1
    long_idx = int((long - long_min) / (long_max - long_min) * cols)
    return long_idx, lat_idx


"""If detailed is equal to 1 this function returns information on all the Soil profiles located at a 30 by 30 arc second 
grid coordinate in the globe provided longitudinal coords between -180 and 180 and latitudinal coords between -90 and 90 
otherwise if detailed is not equal to 1 this function returns information on the the dominant Soil profile at the grid 
coordinate.

Parameters:
long (float): the longitudinal coordinate
lat (float): the latitudinal coordinate
detailed (int): if 1 returns all the Soil profiles, if not 1 returns only the dominant Soil profile
folder (str): the path to this directory for when this function is called from outside this directory

Returns:
Dictionary of (str) keys of a dictionary (str) keys of a (dict) of Soil information values or if there is no data 
returns None

Note: The first set of string keys are composed of a profile ID code 4-5 length e.g. PLe/B a space and then the 
proportion of Soil it covers in a map unit e.g. 70. The second set of keys contains the layer of the Soil e.g. D1. The
dictionary return for each layer contains information on Soil ph, soil_texture, and Soil salinity.

Errors: Calls coordsToPixels so displays an assertion error of long is not between 180 and -180 or if lat is not between 
90 and -90"""


def getSoilData(long, lat, detailed, folder):
    # finds the dimensions of the raster file and accesses the data.
    raster = gdal.Open(f"{folder}/WISE30sec/Interchangeable_format/wise_30sec_v1.tif")
    rows = raster.RasterYSize
    cols = raster.RasterXSize
    band = raster.GetRasterBand(1)
    data = band.ReadAsArray(0, 0, cols, rows)

    # finds the map code associated with the pixel
    x, y = coordsToPixels(long, lat, rows, cols)

    # finds the value of the pixel
    pixels = pd.read_csv(f"{folder}/WISE30sec/Interchangeable_format/wise_30sec_v1.tsv", sep='\t')
    pixel = pixels.loc[pixels["pixel_vaue"] == data[y][x]]

    # if there is no data at the pixel returns None
    if pixel.get("pixel_vaue").values[0] == 0:
        return None

    # finds the map code associated with the pixel
    map_code = pixel.get("description").values[0]

    # finds the number of Soil profiles associated with the map code
    map_units = pd.read_csv(f"{folder}/WISE30sec/Interchangeable_format/HW30s_MapUnit.txt", sep=',', dtype=str)
    soil_record = map_units.loc[map_units["NEWSUID"] == map_code]
    no_profiles = int(soil_record.get("NoSoilComp").values[0])
    if no_profiles == 0:
        return None

    # accesses the data from either all of the Soil profiles or just the dominant one depending on the value of detailed
    soil_profiles = {}
    profiles_file = pd.read_csv(f"{folder}/WISE30sec/Interchangeable_format/HW30s_ParEst.txt", sep=',', dtype=str)
    largest = 0
    dom_profile = ""
    for i in range(1, no_profiles + 1):
        profile = soil_record.get("PRID" + str(i)).values[0]
        prop = int(soil_record.get("PROP" + str(i)).values[0])
        if detailed == 1:
            soil_profiles[profile + " " + str(prop)] = readProfile(profile, profiles_file)
        else:
            if largest < prop:
                largest = prop
                dom_profile = profile
    if detailed != 1:
        soil_profiles[dom_profile + " " + str(largest)] = readProfile(dom_profile, profiles_file)
    return soil_profiles


"""Takes a Soil profile and returns a dictionary of key value pairs where the key is the Soil layer and the pandas 
 dataframe for that layer is the data for that Soil layer. Function should only be called from within getSoilData.
 
 Parameters:
 profile (str): the Soil profile for which we are trying to access data from
 profiles_file (pandas dataframe): the data we are accessing from
 
 Returns:
 A dictionary of (str)layers and a (dict)dictionary of Soil information as values"""


def readProfile(profile, profiles_file):

    # finds the associated layers with the profile
    layers = profiles_file.loc[profiles_file["PRID"] == profile]
    result = {}
    # returns a dictionary containing all the information on all the layers associated with the profile
    for i in range(1, 8):
        info = {}
        layer = layers.loc[layers["Layer"] == "D" + str(i)]
        info["ph"] = layer.loc[:, ["PHAQ"]].values[0][0]
        info["soil_texture"] = []
        info["soil_texture"].append(layer.loc[:, ["PSCL"]].values[0][0])
        # calculates the Soil salinity
        info["soil_salinity"] = float(layer.loc[:, ["ESP"]].values[0][0]) / float(layer.loc[:, ["ECEC"]].values[0][0])
        # determines if the Soil is classed as organic
        if float(layer.loc[:, ["ORGC"]].values[0][0]) / (float(layer.loc[:, ["TOTN"]].values[0][0]) *
                                                         float(layer.loc[:, ["CNrt"]].values[0][0])) > 0.12:
            info["soil_texture"].append("O")
        result["D" + str(i)] = info
    return result
