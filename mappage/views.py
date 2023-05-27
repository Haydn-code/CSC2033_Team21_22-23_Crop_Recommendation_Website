from flask import Blueprint, render_template, request, jsonify

#from DataAccess.Climate.ClimateData import getWeatherData, avgAnnualWeather

from mappage.Forms import mapForm

mappage_blueprint = Blueprint('Mappage', __name__, template_folder='Frontend')


@mappage_blueprint.route('/mappage', methods=["GET", "POST"])
def map():
    form = mapForm()

    if form.validate_on_submit():
        longitude = form.longitude.data
        latitude = form.latitude.data

        scroll_pos = 820
        loaded_by_form = True

        return render_template('Mappage/map.html', scroll_position=scroll_pos, loaded=loaded_by_form, form=form, min_temp=longitude, max_temp=latitude)

    else:
        return render_template('Mappage/map.html', scroll_position=0, loaded=False, form=form, min_temp="N/A", max_temp="N/A")