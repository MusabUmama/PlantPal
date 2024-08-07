from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
import google.generativeai as genai
import os

DISEASE_MODEL_PATH = 'linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification'

disease_pipe = pipeline("image-classification", model=DISEASE_MODEL_PATH)


def disease_detection(image_path):
    
    disease_result = disease_pipe(image_path)
    predicted_disease = disease_result[0]["label"]

    return predicted_disease


def get_plant_disease_info(disease_name):

    if not disease_name:
        return "No diseases found"

    genai.configure(api_key=os.environ['API_KEY'])
    model = genai.GenerativeModel('gemini-1.5-flash')

    if 'healthy' in disease_name.lower():
        return "The plant is looking healthy and no diseases detected.\n 1. Ensure your plants get the right amount of light. \n2. Water your plants according to their specific needs. \n3. Keep plants in a stable temperature range."

    prompt = (f"you are a plant expert application. give few recommendations in a paragraph for {disease_name} disease within 200 words.")

    response = model.generate_content(prompt)
    
    return response.text

def get_plant_info(plant_name):

    if not plant_name:
        return "No plants detected"
    
    genai.configure(api_key=os.environ['API_KEY'])
    model = genai.GenerativeModel('gemini-1.5-flash')

    prompt = (f"you are a plant expert application. give some information in a paragraph about {plant_name} plant within 150 words")

    response = model.generate_content(prompt)
    
    return response.text
  
