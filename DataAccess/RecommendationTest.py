import unittest
from Recommendation import cropRecommendation, checkPh, checkPrec, checkTemp, summariseProfiles


class MyTestCase(unittest.TestCase):
    def test_checkTemp(self):
        crop = {
            "absolute_min_temp": "20",
            "optimal_max_temp": "30"
        }

        weather = {
            "temp_avg": [22, 25, 28, 29, 30, 30, 27]
        }

        self.assertTrue(checkTemp(crop, weather))

    def test_checkPrec(self):
        crop = {
            "optimal_min_rain": "1000",
            "optimal_max_rain": "2000"
        }

        weather = {
            "prec": [80, 120, 150, 180, 200, 210, 190]
        }

        self.assertTrue(checkPrec(crop, weather))

    def test_checkPh(self):
        crop = {
            "optimal_min_ph": "6",
            "optimal_max_ph": "7"
        }

        soil = {
            "ph": 6.5
        }

        self.assertTrue(checkPh(crop, soil))

    class TestCropRecommendation(unittest.TestCase):
        def test_cropRecommendation(self):
            long = 10.123456
            lat = 20.654321
            crops = {
                'crop1': {
                    'optimal_max_temp': 30,
                    'optimal_max_rain': 100,
                    'optimal_min_ph': 5.5
                },
                'crop2': {
                    'optimal_max_temp': 35,
                    'optimal_max_rain': 150,
                    'optimal_min_ph': 6.0
                },
                'crop3': {
                    'optimal_max_temp': 25,
                    'optimal_max_rain': 80,
                    'optimal_min_ph': 5.0
                }
            }
            soilPath = 'Soil'
            climatePath = 'Climate/tif_files'

            result = cropRecommendation(long, lat, crops, soilPath, climatePath)

            self.assertIsNotNone(result)
            self.assertIsInstance(result, list)
            self.assertLessEqual(len(result), 5)

            for crop in result:
                self.assertIn(crop, crops)


if __name__ == '__main__':
    unittest.main()

