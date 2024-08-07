import base64
import boto3
import json
import os
from botocore.exceptions import ClientError

def load_data_from_cloud():
    s3 = boto3.client(
        's3'
        #aws_access_key_id="AKIAQE43KD6GWFYQTY7C",
        #aws_secret_access_key="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",
        #region_name='ap-southeast-2'
    )


    try:
        response = s3.list_objects_v2(Bucket='plantpal-data', Prefix='plant_data/')

        if 'Contents' not in response:
            print("No JSON files found in the specified S3 bucket and prefix.")
            return None

        objects = response['Contents']
        objects.sort(key=lambda obj: obj['LastModified'], reverse=True)
        latest_object = objects[0]

        local_dir = os.path.join(os.getcwd(), 'data')
        os.makedirs(local_dir, exist_ok=True)

        local_file_path = os.path.join(local_dir, os.path.basename(latest_object['Key']))
        s3.download_file('plantpal-data', latest_object['Key'], local_file_path)

        print("data loaded")

        return local_file_path

    except ClientError as e:
        print(f"Error loading JSON data from S3: {e}")
        return None


def get_image(path):
    try:
        with open(path, 'r') as f:
            data = json.load(f)

        if 'image' not in data:
            print("Image data not found in JSON file")
            return None

        image_data = base64.b64decode(data['image'])

        image_format = 'jpg'

        output_dir = os.path.join(os.getcwd(), 'pi')
        os.makedirs(output_dir, exist_ok=True)
        filename = f"image_{os.path.basename(path).split('.')[0]}.{image_format}"
        output_path = os.path.join(output_dir, filename)

        with open(output_path, 'wb') as f:
            f.write(image_data)

        return output_path

    except Exception as e:
        print(f"Error saving image: {e}")
        return None


def get_plant_data(path):
    try:
        with open(path, 'r') as f:
            data = json.load(f)

        plant_class = data.get('plant_class')
        soil_moisture = data.get('soil_moisture')

        if plant_class is None or soil_moisture is None:
            print("Missing plant_class or soil_moisture in JSON file")
            return None
        
        plant_class = plant_class.upper()

        return plant_class, soil_moisture

    except FileNotFoundError:
        print("JSON file not found")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON file")
        return None


def check_watering(soil_moisture):
    if soil_moisture == 0.0:
        return "The plant needs watering"
    else:
        return "No watering needed"
