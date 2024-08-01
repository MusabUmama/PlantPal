import uuid
import boto3
import json
import base64
from botocore.exceptions import ClientError


def send_data_to_cloud(plant, soil_moisture, image_path=None):

    s3 = boto3.client(
        's3',
        aws_access_key_id="AKIAQE43KD6GWFYQTY7C",
        aws_secret_access_key="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"
    )

    try:
        data = {

            "plant_class": plant,
            "soil_moisture": soil_moisture
        }

        if image_path:
            with open(image_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
                data['image'] = encoded_string

        data_str = json.dumps(data)

        key = f'plant_data/{uuid.uuid4()}.json'

        s3.put_object(Body=data_str, Bucket='plantpal-data', Key=key)
        print(f"Data sent to cloud: {key}")
    except ClientError as e:
        print(f"Error sending data to cloud: {e}")
