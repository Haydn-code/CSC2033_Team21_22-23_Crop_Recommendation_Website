import csv
import math
import numpy as np
from osgeo import gdal
from DataAccess.Soil import coordsToPixels


"""Finds the closest city to a given longitude and latitude using the Haversine formula.

Parameters:
    long (float): The longitude coordinate for which to find the closest city.
    lat (float): The latitude coordinate for which to find the closest city.

Returns:
    str: The name of the closest city to the given coordinates, as
         found in the 'worldcities.csv' file.
"""


def findClosestCity(long, lat):
    with open('worldcities.csv', newline='', encoding='utf-8') as cities_file:
        cities_reader = csv.DictReader(cities_file)

        closest_city = None
        smallest_distance = float('inf')

        for row in cities_reader:
            city_lat = float(row['lat'])
            city_long = float(row['lng'])

            # Calculate the distance between the input coordinates and the city
            earth_radius = 6371  # Earth's radius in km
            lat_distance = math.radians(city_lat - lat)
            lng_distance = math.radians(city_long - long)
            a = math.sin(lat_distance / 2) ** 2 + math.cos(math.radians(lat)) * math.cos(math.radians(city_lat)) * math.sin(lng_distance / 2) ** 2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            distance = earth_radius * c

            # Update the closest city if a closer one has been found
            if distance < smallest_distance:
                smallest_distance = distance
                closest_city = row['city']

        return closest_city


"""Extracts weather data from geotiff files for a given longitude and latitude.

Parameters:
long (float): The longitude coordinate for which to extract weather data.
lat (float): The latitude coordinate for which to extract weather data.
folder (str): The path to the folder containing the geotiff files.

Returns:
weather_dict (dict): A dictionary containing the extracted weather data. The keys of the
                     dictionary are the weather categories ('prec', 'srad', 'temp_avg',
                     'temp_max', 'temp_min', 'wind'), and the values are lists of
                     values representing the monthly weather data for the given location.
"""


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
