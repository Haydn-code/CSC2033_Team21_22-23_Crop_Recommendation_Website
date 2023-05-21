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


def cropRecommendation(long, lat, crops, soilPath, climatePath):
    profiles = getSoilData(long, lat, 1, "Soil")
    print(profiles)
    combined = summariseProfiles(profiles)
    print(combined)
    #weather = getWeatherData(long, lat, "Climate/tif_files")
    #print(weather)


cropRecommendation(0, 0, "crops", "Soil", "Climate/tif_files")