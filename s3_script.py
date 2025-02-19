import json
import boto3
import paho.mqtt.client as mqtt
from datetime import datetime

# AWS S3 client
s3_client = boto3.client('s3', region_name='eu-north-1')
bucket_name = "your-s3-bucket-name"  # Replace with your actual bucket name

# MQTT settings
mqtt_broker = "51.20.85.183" #Replace with your broker IP
mqtt_port = 1883 # Replace with your broker port
mqtt_topic = "test"  # Replace with your topic

# Callback function to handle incoming MQTT messages
def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")

    try:
        # Parse JSON message
        message = json.loads(msg.payload.decode())

        # Generate a unique filename using timestamp
        timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"mqtt_data/{timestamp}.json"  # Store in "mqtt_data/" folder inside S3

        # Convert message to JSON string
        file_content = json.dumps(message, indent=4)

        # Upload data to S3
        response = s3_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=file_content,
            ContentType="application/json"
        )

        print(f"Data uploaded to S3: {file_name}, Response: {response}")

    except Exception as e:
        print(f"Error processing message: {e}")

# Set up MQTT client
client = mqtt.Client()
client.on_message = on_message

# Connect to MQTT broker
client.connect(mqtt_broker, mqtt_port)

# Subscribe to topic
client.subscribe(mqtt_topic)

# Start the loop to listen for messages
client.loop_forever()
