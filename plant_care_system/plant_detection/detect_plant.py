from transformers import pipeline

PLANT_MODEL_PATH = 'NonoBru/leaf-classifier'

plant_pipe = pipeline("image-classification", model=PLANT_MODEL_PATH, cache_dir='plant_care_system/models')

def plant_classify(image_path):
    
    plant_result = plant_pipe(image_path)
    predicted_plant = plant_result[0]["label"]

    return predicted_plant
