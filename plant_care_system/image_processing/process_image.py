from transformers import pipeline

PLANT_MODEL_PATH = 'NonoBru/leaf-classifier'
DISEASE_MODEL_PATH = 'linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification'

disease_pipe = pipeline("image-classification", model=DISEASE_MODEL_PATH)
plant_pipe = pipeline("image-classification", model=PLANT_MODEL_PATH)

def plant_classify(image_path):
    
    plant_result = plant_pipe(image_path)
    predicted_plant = plant_result[0]["label"]

    return predicted_plant


def disease_detection(image_path):
    
    disease_result = disease_pipe(image_path)
    predicted_disease = disease_result[0]["label"]

    return predicted_disease