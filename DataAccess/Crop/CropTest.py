import unittest
from Crop import getCrops, searchCrop


class MyTestCase(unittest.TestCase):
    crops = getCrops("Crop")

    def test_get_crops(self):
        self.assertEquals(type(self.crops), dict)

    def test_searchCrop(self):
        self.assertEqual(searchCrop("tomato", self.crops, False), {'optimal_max_temp': '27', 'absolute_max_temp': '35',
        'optimal_min_temp': '20', 'absolute_min_temp': '7', 'optimal_max_ph': '6.8', 'absolute_max_ph': '7.5',
        'optimal_min_ph': '5.5', 'absolute_min_ph': '5', 'optimal_max_rain': '1300', 'absolute_max_rain': '1800',
        'optimal_min_rain': '600', 'absolute_min_rain': '400', 'optimal_texture': 'medium, organic',
        'absolute_texture': 'heavy, medium, light', 'optimal_salinity': 'low (<4 dS/m)', 'absolute_salinity':
        'low (<4 dS/m)', 'photoperiod': 'short day (<12 hours), neutral day (12-14 hours), long day (>14 hours)',
        'common_names': 'tomato, tomate, pomodoro, tomata, tomatar, temata, temeta, tamatie', 'species':
        'Lycopersicon esculentum', 'life_form': 'herb', 'life_span': 'annual', 'physiology': 'single stem',
        'plant_attributes': 'grown on large scale', 'absolute_min_altitude': '-', 'absolute_max_altitude': '2400',
        'optimal_min_light': 'clear skies', 'optimal_max_light': 'clear skies', 'optimal_depth': 'shallow (20-50 cm)',
        'optimal_fertility': 'high', 'optimal_drainage': 'well (dry spells)', 'absolute_drainage': 'well (dry spells)',
        'climate_zone': 'tropical wet & dry (Aw), tropical wet (Ar), steppe or semiarid (Bs), subtropical humid (Cf), '
        'subtropical dry summer (Cs), subtropical dry winter (Cw), temperate oceanic (Do), temperate continental (Dc), '
        'temperate with humid winters (Df), temperate with dry winters (Dw)', 'main_use': 'food & beverage',
        'category': 'forage/pasture, vegetables, medicinals & aromatic',
        'image': 'https://ecocrop.review.fao.org/ecocrop/ec_images/1379.jpg'})
        self.assertEqual(searchCrop("Abelmoschus esculentus", self.crops, True), {'optimal_max_temp': '30',
        'absolute_max_temp': '35', 'optimal_min_temp': '20', 'absolute_min_temp': '12', 'optimal_max_ph': '7',
        'absolute_max_ph': '8.7', 'optimal_min_ph': '5.5', 'absolute_min_ph': '4.5', 'optimal_max_rain': '1200',
        'absolute_max_rain': '2500', 'optimal_min_rain': '600', 'absolute_min_rain': '300', 'optimal_texture':
        'heavy, medium, light, organic', 'absolute_texture': 'heavy, medium, light', 'optimal_salinity': 'low (<4 dS/m)'
        , 'absolute_salinity': 'low (<4 dS/m)', 'photoperiod': 'short day (<12 hours)', 'common_names':
        "abelmoskus, america-neri, bakhua mun, bamia, bamija, bamya, bandakai, bende', bhindee, bhindi, bindi, bumbo, "
        "bunga depros, calulu', cantarella, chaucha turca, dâu bap, Eibisch, frutto d‚ibisco, gobbo, gombaut, gombo, "
        "Gombro, haluyoy, huang qiu kui, ibisco, kacang bendi, kacang lender, kembang dapros, ketmie comestible, "
        "kopi arab, krachiap man, krachiapkhieo, lady fingers, lady's finger, mesta, ocra, okay, oker, okra, okro, "
        "okura, quiabo, quimbambo, quimgombó, quingombo, ramturai, rosenapfel, saluyota bunga, sayur bendi, tori, "
        "tuah lek, vendakai, yong kok dau", 'species': 'Abelmoschus esculentus', 'life_form': 'herb',
        'life_span': 'annual', 'physiology': 'single stem', 'plant_attributes': 'grown on large scale',
        'absolute_min_altitude': '-', 'absolute_max_altitude': '1000', 'optimal_min_light': 'clear skies',
        'optimal_max_light': 'clear skies', 'optimal_depth': 'shallow (20-50 cm)', 'optimal_fertility': 'high',
        'optimal_drainage': 'well (dry spells)', 'absolute_drainage': 'well (dry spells)', 'climate_zone':
        'tropical wet & dry (Aw), tropical wet (Ar), steppe or semiarid (Bs), subtropical humid (Cf), subtropical dry '
        'summer (Cs), subtropical dry winter (Cw)', 'main_use': 'food & beverage', 'category': 'vegetables',
        'image': 'https://ecocrop.review.fao.org/ecocrop/ec_images/289.jpg'})


if __name__ == '__main__':
    unittest.main()
