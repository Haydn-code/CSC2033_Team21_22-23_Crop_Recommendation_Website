from Soil.Soil import getSoilData
from Climate.ClimateData import getWeatherData


"""Defined a function that takes all of the crops and provides a summary of the necessary data for crop recommendation 
for each layer, from each profile relative to the percentage of land they take up.

Parameters 
profiles (dict): a dictionary containing information on different soil profiles

Returns: 
A summarised (dict) of ph and soil salinity for each layer of soil
"""


def summariseProfiles(profiles):
    combined = {}
    for i in range(1, 8):
        ph = 0
        soil_salinity = 0
        layer = {}
        for each in profiles:
            percent = int(each[-3:])/100
            profile = profiles.get(each).get("D" + str(i))
            ph += float(profile.get("ph"))*percent
            soil_salinity += float(profile.get("soil_salinity"))*percent
        layer["ph"] = ph
        layer["soil_salinity"] = soil_salinity
        combined["D" + str(i)] = layer
    return combined


"""A function which returns crop information on the most suitable crop to grow at a coordinate

Parameters:
long (float): the longitudinal coordinate
lat (float): the latitudinal coordinate
crops (dict): the dictionary returned from getCrops(folder) in crop.py
soilPath (str): the path to the Soil directory
climatePath (str): the path to the Climate/tif_files directory

Returns:
A (dict) containing information on the recommended crop"""


def cropRecommendation(long, lat, crops, soilPath, climatePath):
    profiles = getSoilData(long, lat, 1, soilPath)
    print(profiles)
    combined = summariseProfiles(profiles)
    print(combined)
    weather = getWeatherData(long, lat, climatePath)
    print(weather)


cropRecommendation(-1.604004, 8.341953, "placeholder", "Soil", "Climate/tif_files")