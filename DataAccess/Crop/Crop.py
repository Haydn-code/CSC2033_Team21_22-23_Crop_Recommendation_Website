import pandas as pd

"""This function returns the necessary info from the Crop dataset for the recommendation algorithm

Returns:
A dictionary of crop_id(str) as keys, with a dictionary of relevant Crop information as values.
"""


def getCrops():
    crops = {}
    # defines Crop uses that address world hunger
    valid_uses = ["vitamins", "protein", "fibres", "lipids/oils & fats", "condiment/seasoning", "minerals", "starch",
                  "essential oils", "lipids", "honey", "sugar", "sweetener", "nutritional applications"]
    plants = pd.read_csv('cropbasics_scrape.csv', sep=',', dtype=str)
    common_names = pd.read_csv('crop_view_data.csv', sep=',', dtype=str)
    for idx, row in plants.iterrows():
        # prevents error from attempting to iterate over float values which can be found.
        if type(row["Plant.attributes"]) == float:
            pass
        # checks that the Crop can be grown on large scale and that its use addresses world hunger
        elif row["use.detailed"] in valid_uses and "grown on large scale" in row["Plant.attributes"]:
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
                    "scientific_name": row["species"]}

            crops[row["crop_code"]] = info
    return crops


"""Function searches the Crop dataset and returns relevant information to the researched Crop

Parameters:
crop_name (string): the common name of a Crop the user is searching for

Returns:
A dictionary of information associated with the searched crop_name or None if the crop_name is not found
"""


def searchCrop(crop_name):
    if crop_name == "nan":
        return None
    crops = getCrops()
    for each in crops:
        crop = crops.get(each)
        names = str(crop.get("common_names")).split(", ")
        if crop_name in names:
            return crop
    return None



