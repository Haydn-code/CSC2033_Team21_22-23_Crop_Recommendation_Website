import unittest
import pandas as pd
from Soil import getSoilData, readProfile, coordsToPixels


class MyTestCase(unittest.TestCase):
    profiles_file = pd.read_csv(f"Soil/WISE30sec/Interchangeable_format/HW30s_ParEst.txt", sep=',', dtype=str)

    def test_read_profile_length_5(self):
        self.assertEqual(readProfile("ACu/B", self.profiles_file), {'D1': {'ph': '4.90', 'soil_texture': ['F', 'O'],
                                                                           'soil_salinity': 0.125},
                                                                    'D2': {'ph': '5.00', 'soil_texture': ['F', 'O'],
                                                                           'soil_salinity': 0.16666666666666666},
                                                                    'D3': {'ph': '5.10', 'soil_texture': ['F', 'O'],
                                                                           'soil_salinity': 0.16666666666666666},
                                                                    'D4': {'ph': '5.10', 'soil_texture': ['F', 'O'],
                                                                           'soil_salinity': 0.16666666666666666},
                                                                    'D5': {'ph': '5.10', 'soil_texture': ['F', 'O'],
                                                                           'soil_salinity': 0.14285714285714285},
                                                                    'D6': {'ph': '5.10', 'soil_texture': ['F', 'O'],
                                                                           'soil_salinity': 0.14285714285714285},
                                                                    'D7': {'ph': '5.20', 'soil_texture': ['F', 'O'],
                                                                           'soil_salinity': 0.14285714285714285}})

    def test_read_profile_length_4(self):
        self.assertEqual(readProfile("AC/B", self.profiles_file), {'D1': {'ph': '5.40', 'soil_texture': ['C', 'O'],
                                                                          'soil_salinity': 1.5},
                                                                   'D2': {'ph': '5.10', 'soil_texture': ['C', 'O'],
                                                                          'soil_salinity': 1.0},
                                                                   'D3': {'ph': '5.10', 'soil_texture': ['M', 'O'],
                                                                          'soil_salinity': 1.0}, 'D4': {'ph': '5.10',
                                                                                                        'soil_texture':
                                                                                                            ['M', 'O'],
                                                                                                        'soil_salinity':
                                                                                                            1.0},
                                                                   'D5': {'ph': '5.10', 'soil_texture': ['M', 'O'],
                                                                          'soil_salinity': 1.0},
                                                                   'D6': {'ph': '5.20', 'soil_texture': ['M', 'O'],
                                                                          'soil_salinity': 1.5},
                                                                   'D7': {'ph': '5.20', 'soil_texture': ['M', 'O'],
                                                                          'soil_salinity': 0.5}})

    def test_coords_to_pixels(self):
        self.assertEqual(coordsToPixels(0, 0, 100, 100), (50, 49))
        self.assertEqual(coordsToPixels(-180, -90, 100, 100), (0, 99))
        self.assertEqual(coordsToPixels(179.9, 89.9, 100, 100), (99, 0))

    def test_get_soil_data(self):
        self.assertEqual(getSoilData(0, 0, 0, "Soil"), {'PLe/B 70': {'D1': {'ph': '6.20', 'soil_texture': ['C', 'O'],
                                                                            'soil_salinity': 0.7142857142857143},
                                                                     'D2': {'ph': '6.40', 'soil_texture': ['M', 'O'],
                                                                            'soil_salinity': 0.6363636363636364},
                                                                     'D3': {'ph': '6.60',
                                                                            'soil_texture': ['M', 'O'],
                                                                            'soil_salinity': 0.5384615384615384},
                                                                     'D4': {'ph': '6.80',
                                                                            'soil_texture': ['M', 'O'],
                                                                            'soil_salinity': 0.5333333333333333},
                                                                     'D5': {'ph': '7.20',
                                                                            'soil_texture': ['M', 'O'],
                                                                            'soil_salinity': 0.38461538461538464},
                                                                     'D6': {'ph': '7.20',
                                                                            'soil_texture': ['M', 'O'],
                                                                            'soil_salinity': 0.25},
                                                                     'D7': {'ph': '7.30', 'soil_texture': ['M', 'O'],
                                                                            'soil_salinity': 0.3888888888888889}}})
        self.assertEqual(getSoilData(0, 0, 1, "Soil"), {'PLe/B 70': {'D1': {'ph': '6.20', 'soil_texture': ['C', 'O'],
                                                                            'soil_salinity': 0.7142857142857143},
                                                                     'D2': {'ph': '6.40', 'soil_texture': ['M', 'O'],
                                                                            'soil_salinity': 0.6363636363636364},
                                                                     'D3': {'ph': '6.60',
                                                                            'soil_texture': ['M', 'O'],
                                                                            'soil_salinity': 0.5384615384615384},
                                                                     'D4': {'ph': '6.80', 'soil_texture': ['M', 'O'],
                                                                            'soil_salinity': 0.5333333333333333},
                                                                     'D5': {'ph': '7.20', 'soil_texture': ['M', 'O'],
                                                                            'soil_salinity': 0.38461538461538464},
                                                                     'D6': {'ph': '7.20', 'soil_texture': ['M', 'O'],
                                                                            'soil_salinity': 0.25},
                                                                     'D7': {'ph': '7.30', 'soil_texture': ['M', 'O'],
                                                                            'soil_salinity': 0.3888888888888889}},
                                                        'LVg/B 30': {'D1': {'ph': '6.60', 'soil_texture': ['M', 'O'],
                                                                            'soil_salinity': 0.1111111111111111},
                                                                     'D2': {'ph': '6.80', 'soil_texture': ['M', 'O'],
                                                                            'soil_salinity': 0.15},
                                                                     'D3': {'ph': '6.90', 'soil_texture': ['M', 'O'],
                                                                            'soil_salinity': 0.14285714285714285},
                                                                     'D4': {'ph': '7.00', 'soil_texture': ['M', 'O'],
                                                                            'soil_salinity': 0.13043478260869565},
                                                                     'D5': {'ph': '7.30', 'soil_texture': ['M', 'O'],
                                                                            'soil_salinity': 0.15384615384615385},
                                                                     'D6': {'ph': '7.00', 'soil_texture': ['M', 'O'],
                                                                            'soil_salinity': 0.125},
                                                                     'D7': {'ph': '6.80', 'soil_texture': ['M', 'O'],
                                                                            'soil_salinity': 0.22727272727272727}}})


if __name__ == '__main__':
    unittest.main()
