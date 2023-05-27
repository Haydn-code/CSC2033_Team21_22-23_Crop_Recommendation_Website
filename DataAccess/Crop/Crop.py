import pandas as pd
import requests
from bs4 import BeautifulSoup

"""This function returns the necessary info from the Crop dataset for the recommendation algorithm

Parameters:
folder (str): the path to this directory for when this function is called from outside this directory

Returns:
A dictionary of crop_id(str) as keys, with a dictionary of relevant Crop information as values.
"""


def getCrops(folder):
    crops = {}
    # defines Crop uses that address world hunger
    valid_uses = ["vitamins", "protein", "fibres", "lipids/oils & fats", "condiment/seasoning", "minerals", "starch",
                  "essential oils", "lipids", "honey", "sugar", "sweetener", "nutritional applications"]
    plants = pd.read_csv(f"{folder}/cropbasics_scrape.csv", sep=',', dtype=str)
    common_names = pd.read_csv(f"{folder}/crop_view_data.csv", sep=',', dtype=str)
    for idx, row in plants.iterrows():
        # prevents error from attempting to iterate over float values which can be found.
        if type(row["Plant.attributes"]) == float:
            pass
        # checks that the Crop can be grown on large scale and that its use addresses world hunger
        elif row["use.detailed"] in valid_uses and ("grown on large scale" in row["Plant.attributes"] or
                                                    "grown on small scale" in row["Plant.attributes"]):
            print(row)
            # collects the relevant info for the Crop and assigns to dict
            info = {"optimal_max_temp": row["Temp_Opt_Max"], "absolute_max_temp": row["Temp_Abs_Max"],
                    "optimal_min_temp": row["temp_opt_min"], "absolute_min_temp": row["Temp_Abs_Min"],
                    "optimal_max_ph": row["pH_Opt_Max"], "absolute_max_ph": row["pH_Abs_Max"],
                    "optimal_min_ph": row["pH_Opt_Min"], "absolute_min_ph": row["pH_Abs_Min"],
                    "optimal_max_rain": row["Rain_Opt_Max"], "absolute_max_rain": row["Rain_Abs_Max"],
                    "optimal_min_rain": row["Rain_Opt_Min"], "absolute_min_rain": row["Rain_Abs_Min"],
                    "optimal_texture": row["Texture_Ops"], "absolute_texture": row["Texture_Abs"],
                    "optimal_salinity": row["Salinity_Ops"], "absolute_salinity": row["Salinity_Abs"],
                    "photoperiod": row["photoperiod"], "common_names":
                        common_names.loc[common_names["Ecocrop_code"] == row["crop_code"]]["Common_names"].values[0],
                    "species": row["species"], "life_form": row["Life.form"], "life_span": row["Life.span"],
                    "physiology": row["Physiology"], "plant_attributes": row["Plant.attributes"],
                    "absolute_min_altitude": row["Alt_Abs_Min"], "absolute_max_altitude": row["Alt_Abs_Max"],
                    "optimal_min_light": row["Light_Opt_Min"], "optimal_max_light": row["Light_Opt_Max"],
                    "optimal_depth": row["Depth_Opt"], "optimal_fertility": row["Fertility_Ops"],
                    "optimal_drainage": row["drainage_opt"], "absolute_drainage": row["drainage_abs"],
                    "climate_zone": row["Climate.Zone"], "main_use": row["use.main"], "category": row["Category"]}

            crops[row["crop_code"]] = info
    return crops


"""Function searches the Crop dataset and returns relevant information to the researched Crop

Parameters:
crop_name (string): the common name of a Crop the user is searching for
crops (dict): the information on all crops extracted from the database
scientific (bool): True if searching by scientific name and False if searching by common name

Returns:
A dictionary of information associated with the searched crop_name or None if the crop_name is not found

Note: crops should be a variable containing the return value from getCrops()
"""


def searchCrop(crop_name, crops, scientific):
    print(crop_name)
    if crop_name == "nan":
        return None
    if not scientific:
        for each in crops:
            crop = crops.get(each)
            names = str(crop.get("common_names")).split(", ")
            if crop_name in names:
                img = requests.get("https://ecocrop.review.fao.org/ecocrop/ec_images/" + each + ".jpg")
                if img.status_code == 200:
                    crop["image"] = "https://ecocrop.review.fao.org/ecocrop/ec_images/" + each + ".jpg"

                else:
                    crop["image"] = "https://ecocrop.review.fao.org/ecocrop/ec_images/" + each + ".gif"
                return crop
    else:
        for each in crops:
            crop = crops.get(each)
            if crop_name == crop.get("species"):
                img = requests.get("https://ecocrop.review.fao.org/ecocrop/ec_images/" + each + ".jpg")
                if img.status_code == 200:
                    crop["image"] = "https://ecocrop.review.fao.org/ecocrop/ec_images/" + each + ".jpg"
                else:
                    crop["image"] = "https://ecocrop.review.fao.org/ecocrop/ec_images/" + each + ".gif"
                return crop
    return None
