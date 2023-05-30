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
                                                                                                        'soil_texture': [
                                                                                                            'M', 'O'],
                                                                                                        'soil_salinity': 1.0},
                                                                   'D5': {'ph': '5.10', 'soil_texture': ['M', 'O'],
                                                                          'soil_salinity': 1.0},
                                                                   'D6': {'ph': '5.20', 'soil_texture': ['M', 'O'],
                                                                          'soil_salinity': 1.5},
                                                                   'D7': {'ph': '5.20', 'soil_texture': ['M', 'O'],
                                                                          'soil_salinity': 0.5}})

    def test_coords_to_pixels(self):
        self.assertEqual()

if __name__ == '__main__':
    unittest.main()
