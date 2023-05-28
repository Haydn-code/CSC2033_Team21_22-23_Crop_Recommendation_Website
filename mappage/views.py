from flask import Blueprint, render_template, request, jsonify
#from DataAccess.Climate.ClimateData import getWeatherData, avgAnnualWeather, findClosestCity
import os

print(os.getcwd())
#from DataAccess.Soil.Soil import getSoilData
from DataAccess.Crop.Crop import getCrops
#from DataAccess.Recommendation import cropRecommendation,summariseProfiles
from mappage.Forms import mapForm
import numpy as np
from Models import Fields
from flask_login import current_user

mappage_blueprint = Blueprint('Mappage', __name__, template_folder='Frontend')


@mappage_blueprint.route('/mappage', methods=["GET", "POST"])
def map():
    form = mapForm()
    num_of_fields = 0
    name_list = []
    longitude_list = []
    latitude_list = []

    if form.validate_on_submit():

        if Fields.userID == current_user.id:
            num_of_fields = Fields.query.filter_by(userID=current_user.id).count()

            farm = Fields.query.filter_by(userID=current_user.id).all()
            name_list = [fields.name for fields in farm]
            longitude_list = [fields.longitude for fields in farm]
            latitude_list = [fields.latitude for fields in farm]


        longitude = float(form.longitude.data)
        latitude = float(form.latitude.data)
        soil = getSoilData(longitude, latitude, 0, "DataAccess/Soil")
        if soil != None:
            combined = summariseProfiles(soil)
            soil_salinity = combined.get("D1").get("soil_salinity")
            soil_ph = combined.get("D1").get("soil_ph")
            soil_texture = soil.get(list(soil.keys())[0]).get("D1").get("soil_texture")
        else:
            soil_salinity = "N/A"
            soil_ph = "N/A"
            soil_texture = "N/A"
        climate = avgAnnualWeather(getWeatherData(longitude, latitude, "DataAccess/Climate/tif_files"))
        if climate is not None:
            min_temp = climate.get("annual_temp_min")
            max_temp = climate.get("annual_temp_max")
            avg_temp = climate.get("annual_temp_avg")
            solar_rad = climate.get("annual_srad")
            avg_wind = climate.get("annual_wind")
            avg_rain = climate.get("annual_prec")
        else:
            min_temp = "N/A"
            max_temp = "N/A"
            avg_temp = "N/A"
            solar_rad = "N/A"
            avg_wind = "N/A"
            avg_rain = "N/A"
        recommend = ""
        test = cropRecommendation(longitude, latitude, getCrops("DataAccess/Crop"),
                                       "DataAccess/Soil",
                                       "DataAccess/Climate/tif_files")
        if test is not None:
            for each in test:
                recommend += each.get("species") + ", "
        country_name = form.country_name.data
        continent_name = form.continent_name.data

        scroll_pos = 820
        loaded_by_form = True

        return render_template('Mappage/map.html', scroll_position=scroll_pos, loaded=loaded_by_form, form=form,
                               close_city=findClosestCity(longitude, latitude, "DataAccess/Climate"), min_temp=min_temp,
                               max_temp=max_temp, avg_temp=avg_temp, solar_rad=solar_rad, avg_wind=avg_wind,
                               avg_rain=avg_rain, soil_salinity=soil_salinity, soil_ph=soil_ph,
                               soil_texture=soil_texture, recommendation=recommend, name_country=country_name,
                               name_continent=continent_name,
                               num_of_markers=num_of_fields, marker_lng=longitude_list, marker_lat=latitude_list,
                               marker_name=name_list)

    else:
        return render_template('Mappage/map.html', scroll_position=0, loaded=False, form=form, min_temp="N/A",
                               max_temp="N/A",
                               num_of_markers=num_of_fields, marker_lng=longitude_list, marker_lat=latitude_list,
                               marker_name=name_list
                               )
