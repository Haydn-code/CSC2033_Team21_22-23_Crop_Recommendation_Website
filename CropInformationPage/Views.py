from flask import Blueprint, render_template

from DataAccess.Crop.Crop import getCrops, searchCrop
from CropInformationPage.Forms import searchCropForm

cropinformation_blueprint = Blueprint('Cropinformationpage', __name__, template_folder='Frontend')


@cropinformation_blueprint.route('/cropinformationpage', methods=["POST", "GET"])
def cropinfromationpage():
    form = searchCropForm()

    # checks to see if the user has searched for a crop
    if form.validate_on_submit():

        # gets a dictionary of all food crops we would potentially recommend
        crops = getCrops("DataAccess/Crop")

        # searches for crop by scientific name
        crop = searchCrop(form.search.data, crops, True)

        scroll_pos = 820
        loaded_by_form = True

        # if found renders the webpage with information about the crop
        if crop is not None:
            return render_template('Cropinformationpage/crop-information.html', scroll_position=scroll_pos,
                                   loaded=loaded_by_form, form=form, search="Search...", image=crop.get("image"),
                                   name=form.search.data, species=crop.get("species"), life_form=crop.get("life_form"),
                                   category=crop.get("category"), life_span=crop.get("life_span"),
                                   physiology=crop.get("physiology"), attributes=crop.get("plant_attributes"),
                                   main_use=crop.get("main_use"), opt_min_temp=crop.get("optimal_min_temp"),
                                   opt_max_temp=crop.get("optimal_max_temp"), abs_min_temp=crop.get("absolute_min_temp")
                                   , abs_max_temp=crop.get("absolute_max_temp"),
                                   opt_min_rain=crop.get("optimal_min_rain"), opt_max_rain=crop.get("optimal_max_rain"),
                                   abs_min_rain=crop.get("absolute_min_rain"),
                                   abs_max_rain=crop.get("absolute_max_rain"), opt_min_ph=crop.get("optimal_min_ph"),
                                   opt_max_ph=crop.get("optimal_max_ph"), abs_min_ph=crop.get("absolute_min_ph"),
                                   abs_max_ph=crop.get("absolute_max_ph"), abs_min_alt=crop.get("absolute_min_altitude")
                                   , abs_max_alt=crop.get("absolute_max_altitude"),
                                   opt_min_light=crop.get("optimal_min_light"),
                                   opt_max_light=crop.get("optimal_max_light"), opt_sal=crop.get("optimal_salinity"),
                                   opt_drain=crop.get("optimal_drainage"), opt_depth=crop.get("optimal_depth"),
                                   opt_text=crop.get("optimal_texture"), opt_fert=crop.get("optimal_fertility"),
                                   clim_zone=crop.get("climate_zone"))

        # searches for crop by common name
        crop = searchCrop(form.search.data.lower(), crops, False)

        # if found renders the webpage with information about the crop
        if crop is not None:
            return render_template('Cropinformationpage/crop-information.html', scroll_position=scroll_pos,
                                   loaded=loaded_by_form, form=form, search="Search...", image=crop.get("image"),
                                   name=form.search.data, species=crop.get("species"), life_form=crop.get("life_form"),
                                   category=crop.get("category"), life_span=crop.get("life_span"),
                                   physiology=crop.get("physiology"), attributes=crop.get("plant_attributes"),
                                   main_use=crop.get("main_use"), opt_min_temp=crop.get("optimal_min_temp"),
                                   opt_max_temp=crop.get("optimal_max_temp"), abs_min_temp=crop.get("absolute_min_temp")
                                   , abs_max_temp=crop.get("absolute_max_temp"),
                                   opt_min_rain=crop.get("optimal_min_rain"), opt_max_rain=crop.get("optimal_max_rain"),
                                   abs_min_rain=crop.get("absolute_min_rain"),
                                   abs_max_rain=crop.get("absolute_max_rain"), opt_min_ph=crop.get("optimal_min_ph"),
                                   opt_max_ph=crop.get("optimal_max_ph"), abs_min_ph=crop.get("absolute_min_ph"),
                                   abs_max_ph=crop.get("absolute_max_ph"), abs_min_alt=crop.get("absolute_min_altitude")
                                   , abs_max_alt=crop.get("absolute_max_altitude"),
                                   opt_min_light=crop.get("optimal_min_light"),
                                   opt_max_light=crop.get("optimal_max_light"), opt_sal=crop.get("optimal_salinity"),
                                   opt_drain=crop.get("optimal_drainage"), opt_depth=crop.get("optimal_depth"),
                                   opt_text=crop.get("optimal_texture"), opt_fert=crop.get("optimal_fertility"),
                                   clim_zone=crop.get("climate_zone"))

        # if there is no such crop renders the webpage N/A to clearly display no such crop was found
        else:
            return render_template('Cropinformationpage/crop-information.html', scroll_position=scroll_pos,
                                   loaded=loaded_by_form, form=form, search="Search...", image="",
                                   name=form.search.data, species="n/a", life_form="n/a", category="n/a",
                                   life_span="n/a", physiology="n/a", attributes="n/a", main_use="n/a",
                                   opt_min_temp="n/a", opt_max_temp="n/a", abs_min_temp="n/a", abs_max_temp="n/a",
                                   opt_min_rain="n/a", opt_max_rain="n/a", abs_min_rain="n/a", abs_max_rain="n/a",
                                   opt_min_ph="n/a", opt_max_ph="n/a", abs_min_ph="n/a", abs_max_ph="n/a",
                                   abs_min_alt="n/a", abs_max_alt="n/a", opt_min_light="n/a", opt_max_light="n/a",
                                   opt_sal="n/a", opt_drain="n/a", opt_depth="n/a", opt_text="n/a", opt_fert="n/a",
                                   clim_zone="n/a")

    # loads initial information to be displayed to the user on initial load of the webpage
    return render_template('Cropinformationpage/crop-information.html', form=form, search="Search...",
                           image="https://ecocrop.review.fao.org/ecocrop/ec_images/289.jpg",
                           name="Okra", species="Abelmoschus esculentus", life_form="Herb", category="Vegetables",
                           life_span="Annual", physiology="Single stem", attributes="Grown on large scale",
                           main_use="Food & beverage", opt_min_temp="20", opt_max_temp="30", abs_min_temp="12",
                           abs_max_temp="35", opt_min_rain="600", opt_max_rain="1200", abs_min_rain="300",
                           abs_max_rain="2500", opt_min_ph="5.5", opt_max_ph="7", abs_min_ph="4.5", abs_max_ph="8.7",
                           abs_min_alt="-", abs_max_alt="1000", opt_min_light="Clear skies", opt_max_light="Clear skies"
                           , opt_sal="low (<4 dS/m)", opt_drain="Well (dry spells)", opt_depth="Shallow (20-50 cm)",
                           opt_text="Heavy, medium, light, organic", opt_fert="High",
                           clim_zone="Tropical wet & dry (Aw), tropical wet (Ar), steppe or semiarid (Bs), " +
                                     "subtropical humid (Cf), subtropical dry summer (Cs), subtropical dry winter (Cw)")
