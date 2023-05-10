import csv
import math


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
