import unittest
from ClimateData import getWeatherData, avgAnnualWeather, findClosestCity


class MyTestCase(unittest.TestCase):

    def test_findClosestCity(self):
        longitude = -1.5927327331271712
        latitude = 54.990737468200415

        expected_city = "Newcastle"

        result = findClosestCity(longitude, latitude)
        self.assertEqual(result, expected_city)

    def test_getWeatherData(self):
        folder = "tif_files"
        longitude = -1.5927327331271712
        latitude = 54.990737468200415

        expected_weather = {
            'prec': [55, 38, 54, 47, 48, 50, 48, 61, 56, 53, 57, 57],
            'srad': [2041, 4237, 8075, 12408, 16808, 17202, 16664, 13582, 9565, 5444, 2631, 1485],
            'temp_avg': [4.151, 4.397, 5.8059998, 7.154, 9.895, 12.9470005, 15.252, 15.078, 12.797, 9.839, 6.754, 5.091],
            'temp_max': [6.869, 7.195, 9.255, 10.967, 14.154, 17.291, 19.715, 19.415, 16.626, 13.214, 9.552, 7.758],
            'temp_min': [1.427, 1.59, 2.354, 3.341, 5.642, 8.614, 10.785, 10.746, 8.982, 6.468, 3.95, 2.431],
            'wind': [5.769, 5.521, 5.501, 4.833, 4.455, 4.181, 3.92, 3.968, 4.532, 4.747, 5.033, 5.255]
        }

        result = getWeatherData(longitude, latitude, folder)
        self.maxDiff = None
        self.assertEqual(result, expected_weather)

    def test_avgAnnualWeather(self):
        weather_dict = {
            'prec': [32, 45, 56, 34, 29, 0, 0, 0, 10, 45, 54, 40],
            'srad': [18, 18, 21, 23, 26, 27, 27, 27, 26, 24, 20, 17],
            'temp_avg': [12, 13, 14, 16, 19, 21, 22, 22, 21, 18, 14, 12],
            'temp_max': [15, 16, 17, 20, 23, 26, 28, 28, 26, 23, 18, 15],
            'temp_min': [9, 9, 10, 11, 12, 14, 15, 15, 14, 12, 10, 9],
            'wind': [8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 8, 8]
        }

        expected_avg_weather = {
            'annual_prec': 29,
            'annual_srad': 23,
            'annual_temp_avg': 17,
            'annual_temp_max': 22,
            'annual_temp_min': 12,
            'annual_wind': 9
        }

        result = avgAnnualWeather(weather_dict)
        self.assertEqual(result, expected_avg_weather)


if __name__ == '__main__':
    unittest.main()
