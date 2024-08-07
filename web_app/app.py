import os
import shutil
import logging
from flask import Flask, render_template, request, url_for
from load_data.load_data import load_data_from_cloud, get_image, get_plant_data, check_watering
from plants.plant_models import get_plant_disease_info, disease_detection, get_plant_info

app = Flask(__name__)

app.config['IMAGE_DIR'] = 'static/captures'

logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    plant_class = None
    soil_moisture = None
    disease_info = None
    watering_message = None
    image_filename = None
    disease_name = None
    
    try:
        
        data_path = load_data_from_cloud()
        if data_path:
            image_path = get_image(data_path)
            plant_class, soil_moisture = get_plant_data(data_path)
            plant_info = get_plant_info(plant_class)
            watering_message = check_watering(soil_moisture)
            
            if image_path:
                disease_name = disease_detection(image_path)
                disease_info = get_plant_disease_info(disease_name)
                image_filename = os.path.basename(image_path)
                image_dest = os.path.join(app.config['IMAGE_DIR'], image_filename)

                os.makedirs(app.config['IMAGE_DIR'], exist_ok=True)
                    
                shutil.copy(image_path, image_dest)

    except Exception as e:
            logging.error(f"An error occurred: {e}")
            return render_template("error.html", error_message="An error occurred while processing the data.")

    return render_template("dashboard.html", 
                           soil_moisture=soil_moisture, 
                           plant_class=plant_class,
                           plant_info=plant_info, 
                           disease_name=disease_name, 
                           disease_info=disease_info, 
                           watering_message=watering_message, 
                           image_url=url_for('static', filename=f'captures/{image_filename}') if image_filename else None)

if __name__ == "__main__":
    app.run(debug=False)
