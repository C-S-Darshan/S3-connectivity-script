# S3-connectivity-script

Steps
1. Update packages and install Mosquitto
##Update packages
```bash
sudo apt update
```

##Install package updates
```bash
sudo apt upgrade -y
```

##Install Mosquitto MQTT
```bash
sudo apt install mosquitto mosquitto-clients -y
```
> **Note:**Make sure to edit security inbound rules to allow messages on selected port**.
##Modify Mosquitto MQTT Conf
```bash
listener 1883 0.0.0.0
allow_anonymous true
```

##Restart Mosquitto
```bash
sudo systemctl restart mosquitto
```

##Ensure that Mosquitto is running
```bash
sudo systemctl status mosquitto
```

##Testing if Mosquito by subscribing and publishing a message
```bash
mosquitto_sub -h localhost -t sensorData
```
```bash
mosquitto_pub -h localhost -t sensorData -m "Hello MQTT"
```

> **Note:**Create a new user and directly add previlages for "AmazonS3FullAccess"**.
##Installing AWS CLI
```bash
sudo snap install aws-cli –classic
```

##Add your user access details
```bash
aws configure
```
> **Note:**Enter Access key, secret key, region and json**.

##Test Configuration
```bash
aws s3 ls
```

##installing pip for required python packages
```bash
sudo apt install python3-pip
```

##Installing virtual environment to ease up setup
```bash
sudo apt install python3-venv
```
##Creating a virtual environment to ease up setup
```bash
python3 -m venv myenv
```

##Activating the virtual environment
```bash
source myenv/bin/activate
```
##Installing packages required to run script
```bash
pip install boto3 paho-mqtt
```

##Creating directory for script
 ```bash
mkdir ~/scripts
```
```bash
cd ~/scripts
```

##Creating the script to connect to S3
```bash
nano mqtt_to_s3.py
```

##Running the script
```bash
python mqtt_to_s3.py
```

##Testing S3 connectivity by publishing message
```bash
mosquitto_pub -h 51.20.85.183 -t test -m '{"DeviceID": "Device1", "Timestamp": "2025-02-06T12:00:00Z", "Data": "SampleData"}'
```
