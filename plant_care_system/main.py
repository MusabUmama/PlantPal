from sensors.image_capture import CameraSensor
from sensors.soil_moisture import read_soil_moisture
from plant_detection.detect_plant import plant_classify
from cloud.cloud_connect import send_data_to_cloud
from PIL import Image


moisture = read_soil_moisture()

camera = CameraSensor()
image_array = camera.capture_image()

image = Image.fromarray(image_array)
filename = "/data_storage/capture.jpg"

image.save(filename, "JPEG")


plant_name = plant_classify(image_path="/data_storage/capture.jpg")


store_data = send_data_to_cloud(plant_name, moisture, image_path="/data_storage/capture.jpg")