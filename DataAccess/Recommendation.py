from DataAccess.Climate.ClimateData import getWeatherData
from DataAccess.Soil.Soil import getSoilData
from DataAccess.Crop.Crop import getCrops


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
            percent = int(each[-2:]) / 100
            profile = profiles.get(each).get("D" + str(i))
            ph += float(profile.get("ph")) * percent
            soil_salinity += float(profile.get("soil_salinity")) * percent
        layer["ph"] = ph
        layer["soil_salinity"] = soil_salinity
        combined["D" + str(i)] = layer
    return combined


"""
Checks if the temperature conditions are suitable for a given crop based on the optimal temperature range.

Parameters:
crop (dict): A dictionary containing crop information.
weather (dict): A dictionary containing weather data.

Returns:
bool: True if the temperature conditions are suitable, False otherwise.
"""


def checkTemp(crop, weather):
    temp_min = crop['absolute_min_temp']
    temp_max = crop['optimal_max_temp']

    # check if the temp range is valid number
    if '-' in temp_min or '-' in temp_max or temp_min == '' or temp_max == '' or '---' in temp_min or '---' in temp_max:
        return False

    temp_min = int(temp_min)
    temp_max = int(temp_max)

    for temp in weather['temp_avg']:
        if not (temp_min <= int(temp) <= temp_max):
            return False

    return True


"""
Checks if the rainfall conditions are suitable for a given crop based on the optimal rainfall range.

Parameters:
crop (dict): A dictionary containing crop information.
weather (dict): A dictionary containing weather data.

Returns:
bool: True if the rainfall conditions are suitable, False otherwise.
"""


def checkPrec(crop, weather):
    rain_min = crop['optimal_min_rain']
    rain_max = crop['optimal_max_rain']

    # check if the rain range is valid number
    if '-' in rain_min or '-' in rain_max or rain_min == '' or rain_max == '' or '---' in rain_min or '---' in rain_max:
        return False

    rain_min = int(rain_min)
    rain_max = int(rain_max)
    total_rain = 0

    for rain in weather['prec']:
        rain_value = int(rain)
        total_rain += rain_value

    if not (rain_min <= total_rain <= rain_max):
        return False

    return True


"""
Checks if the ph conditions are suitable for a given crop based on the optimal ph value.

Parameters:
crop (dict): A dictionary containing crop information.
weather (dict): A dictionary containing soil data.

Returns:
bool: True if the ph conditions are suitable, False otherwise.
"""


def checkPh(crop, soil):
    ph_min = crop['optimal_min_ph']
    ph_max = crop['optimal_max_ph']

    # check if the ph range is valid number
    if '-' in ph_min or '-' in ph_max or ph_min == '' or ph_max == '' or '---' in ph_min or '---' in ph_max:
        return False

    ph_min = float(ph_min)
    ph_max = float(ph_max)

    if not (ph_min <= soil['ph'] <= ph_max):
        return False

    return True


"""
Recommends the most suitable crop to grow at a specific coordinate.

Parameters:
long (float): The longitudinal coordinate.
lat (float): The latitudinal coordinate.
crops (dict): A dictionary containing information about crops, obtained from getCrops(folder) function in crop.py.
soilPath (str): The path to the Soil directory.
climatePath (str): The path to the Climate/tif_files directory.

Returns:
list: A list of dictionaries containing information on the recommended crops.
"""


def cropRecommendation(long, lat, crops, soilPath, climatePath):
    profiles = getSoilData(long, lat, 1, soilPath)
    if profiles == None:
        return None
    combined = summariseProfiles(profiles)
    weather = getWeatherData(long, lat, climatePath)

    crop_scores = []

    for crop_code in crops:
        crop = crops[crop_code]

        # checks temperature suitability
        temp_max = crop['optimal_max_temp']
        if checkTemp(crop, weather):

            # checks rainfall suitability
            rain_max = crop['optimal_max_rain']
            if checkPrec(crop, weather):

                # checks soil suitability
                ph_min = crop['optimal_min_ph']
                ph_max = crop['optimal_max_ph']
                if checkPh(crop, combined['D1']):

                    # calculates the crop score
                    temp_total = sum(int(temp) for temp in weather['temp_avg'])
                    temp_avg = temp_total / len(weather['temp_avg'])

                    rain_total = sum(int(rain) for rain in weather['prec'])
                    rain_avg = rain_total / len(weather['prec'])

                    score = (int(temp_max) - temp_avg) + (int(rain_max) - rain_avg) + (
                        float(ph_max) - combined['D1']['ph'])

                    crop_scores.append((crop, score))

    # sorts the crop scores in descending order
    crop_scores.sort(key=lambda x: x[1], reverse=True)

    # returns the top 5 crops
    recommended_crops = [crop_score[0] for crop_score in crop_scores[:5]]
    return recommended_crops

