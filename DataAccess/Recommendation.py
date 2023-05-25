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
            percent = int(each[-3:]) / 100
            profile = profiles.get(each).get("D" + str(i))
            ph += float(profile.get("ph")) * percent
            soil_salinity += float(profile.get("soil_salinity")) * percent
        layer["ph"] = ph
        layer["soil_salinity"] = soil_salinity
        combined["D" + str(i)] = layer
    return combined


def checkTemp(crop, weather):
    temp_min = crop['absolute_min_temp']
    temp_max = crop['optimal_max_temp']

    if '-' in temp_min or '-' in temp_max or temp_min == '' or temp_max == '' or '---' in temp_min or '---' in temp_max:
        return False

    temp_min = int(temp_min)
    temp_max = int(temp_max)

    for temp in weather['temp_avg']:
        if not (temp_min <= int(temp) <= temp_max):
            return False

    return True


def checkPrec(crop, weather):
    rain_min = crop['optimal_min_rain']
    rain_max = crop['optimal_max_rain']

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
        temp_max = crop['optimal_max_temp']
        if checkTemp(crop, weather):

            # Check rainfall suitability
            rain_max = crop['optimal_max_rain']
            if checkPrec(crop, weather):

                # Check soil suitability
                ph_min = crop['optimal_min_ph']
                ph_max = crop['optimal_max_ph']
                if float(ph_min) <= combined['D1']['ph'] <= float(ph_max):

                    # Calculate the crop score
                    temp_total = sum(int(temp) for temp in weather['temp_avg'])
                    temp_avg = temp_total / len(weather['temp_avg'])

                    rain_total = sum(int(rain) for rain in weather['prec'])
                    rain_avg = rain_total / len(weather['prec'])

                    score = (int(temp_max) - temp_avg) + (int(rain_max) - rain_avg) + (
                        float(ph_max) - combined['D1']['ph'])

                    if score > highest_score:
                        highest_score = score
                        recommended_crop = crop

    return recommended_crop

