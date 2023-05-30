import unittest
from ClimateData import getWeatherData, avgAnnualWeather, findClosestCity


class MyTestCase(unittest.TestCase):

    def test_findClosestCity(self):
        longitude = -0.12765
        latitude = 51.5073359

        expected_city = "London"

        result = findClosestCity(longitude, latitude)
        self.assertEqual(result, expected_city)

    def test_getWeatherData(self):
        folder = "tif_files"
        longitude = -0.12765
        latitude = 51.5073359

        expected_weather = {
            'prec': [64, 41, 49, 46, 49, 55, 43, 50, 58, 63, 62, 61],
            'srad': [2495, 4572, 8458, 12703, 16283, 17675, 16892, 14561, 10504, 6172, 3192, 1937],
            'temp_avg': [4.818, 4.888, 6.8980002, 8.849, 12.459, 15.602, 17.997, 17.716, 14.787, 11.187, 7.441, 5.713],
            'temp_max': [7.561, 7.988, 10.594, 13.266, 17.479, 20.667, 23.123, 22.768, 19.156, 14.91, 10.5390005, 8.402],
            'temp_min': [2.07, 1.78, 3.2, 4.428, 7.43, 10.536, 12.876, 12.663, 10.42, 7.455, 4.352, 3.022],
            'wind': [4.382, 4.316, 4.407, 4.069, 3.9320002, 3.593, 3.545, 3.402, 3.513, 3.636, 3.755, 4.046]
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
