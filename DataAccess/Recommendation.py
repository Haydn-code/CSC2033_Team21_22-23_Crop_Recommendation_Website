from Soil.Soil import getSoilData
from Climate.ClimateData import getWeatherData
from Crop.Crop import getCrops


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


def checkTemp(crop, weather):
    temp_min = crop['absolute_min_temp']
    temp_max = crop['optimal_max_temp']
    for temp in weather['temp_avg']:
        if not (temp_min <= temp <= temp_max):
            return False
    return True


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
    combined = summariseProfiles(profiles)
    weather = getWeatherData(long, lat, climatePath)

    recommended_crop = None
    highest_score = -1

    for crop_code in crops:
        crop = crops[crop_code]

        # Check temperature suitability
        temp_min = crop['absolute_min_temp']
        temp_max = crop['optimal_max_temp']
        if temp_min <= weather['temp_avg'] <= temp_max:

            # Check rainfall suitability
            rain_min = crop['optimal_min_rain']
            rain_max = crop['optimal_max_rain']
            if rain_min <= weather['prec'] <= rain_max:

                # Check soil suitability
                ph_min = crop['optimal_min_ph']
                ph_max = crop['optimal_max_ph']
                if ph_min <= combined['D1']['ph'] <= ph_max:

                    # Calculate the crop score
                    score = (temp_max - weather['temp_avg']) + (rain_max - weather['prec']) + (
                                ph_max - combined['D1']['ph'])

                    if score > highest_score:
                        highest_score = score
                        recommended_crop = crop

    return recommended_crop


cropRecommendation(-1.604004, 8.341953, getCrops("Crop"), "Soil", "Climate/tif_files")
