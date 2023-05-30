import unittest
from Recommendation import cropRecommendation, checkPh, checkPrec, checkTemp, summariseProfiles


class MyTestCase(unittest.TestCase):

    def test_summariseProfiles(self):
        profiles = {
            "Profile1": {
                "D1": {"ph": 6.5, "soil_salinity": 0.2},
                "D2": {"ph": 7.0, "soil_salinity": 0.5},
            },
            "Profile2": {
                "D1": {"ph": 6.8, "soil_salinity": 0.3},
                "D2": {"ph": 7.2, "soil_salinity": 0.4},
            }
        }

        expected_result = {
            "D1": {"ph": 6.65, "soil_salinity": 0.25},
            "D2": {"ph": 7.1, "soil_salinity": 0.45}
        }

        result = summariseProfiles(profiles)
        self.assertEqual(result, expected_result)

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

    def test_cropRecommendation(self):
        long = -1.5927327331271712
        lat = 54.990737468200415
        crops = {
            "001": {
                "optimal_max_temp": "30",
                "optimal_max_rain": "2000",
                "optimal_min_ph": "6",
            },
            "002": {
                "optimal_max_temp": "35",
                "optimal_max_rain": "2500",
                "optimal_min_ph": "6.5",
            },
            "003": {
                "optimal_max_temp": "28",
                "optimal_max_rain": "1500",
                "optimal_min_ph": "5.5",
            },
        }
        soilPath = "Soil"
        climatePath = "Climate/tif_files"

        expected_result = ["001", "002"]

        result = cropRecommendation(long, lat, crops, soilPath, climatePath)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['crop_code'], expected_result[0])
        self.assertEqual(result[1]['crop_code'], expected_result[1])


if __name__ == '__main__':
    unittest.main()

