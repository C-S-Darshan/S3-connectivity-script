# S3 Connectivity Script

This guide walks you through setting up an MQTT broker using Mosquitto, configuring AWS S3 to store MQTT messages, and running a Python script to handle the connectivity. It covers package installations, AWS CLI setup, and script execution.

Follow the steps below to get everything set up properly.

---

## Steps to Set Up and Run the Script

### 1. Update and Install Required Packages

#### Update System Packages

```bash
sudo apt update
```

#### Upgrade Installed Packages

```bash
sudo apt upgrade -y
```

#### Install Mosquitto MQTT Broker

```bash
sudo apt install mosquitto mosquitto-clients -y
```

> **Note:** Ensure that the security inbound rules allow messages on the selected port.

---

### 2. Configure Mosquitto MQTT

#### Access Mosquitto Configuration

```bash
sudo nano /etc/mosquitto/mosquitto.conf
```

#### Modify Mosquitto Configuration

Edit the configuration file and allow external connections:

```bash
listener 1883 0.0.0.0
allow_anonymous true
```
> **Note:** To save and exit, press Ctrl + X, then Y, and press Enter.

#### Restart Mosquitto Service

```bash
sudo systemctl restart mosquitto
```

#### Verify Mosquitto is Running

```bash
sudo systemctl status mosquitto
```

#### Test MQTT Messaging

Subscribe to a test topic:

```bash
mosquitto_sub -h localhost -t sensorData
```

Publish a test message:

```bash
mosquitto_pub -h localhost -t sensorData -m "Hello MQTT"
```

---

### 3. Set Up AWS CLI for S3

> **Note:** Create a new IAM user with the **"AmazonS3FullAccess"** permission.

#### Install AWS CLI

```bash
sudo snap install aws-cli --classic
```

#### Configure AWS CLI with User Credentials

```bash
aws configure
```

> **Input the AWS Access Key, Secret Key, Region, and set output format to JSON.**

#### Verify AWS Configuration

```bash
aws s3 ls
```

---

### 4. Install Python and Dependencies

#### Install `pip`

```bash
sudo apt install python3-pip
```

#### Install Virtual Environment

```bash
sudo apt install python3-venv
```

#### Create and Activate Virtual Environment

```bash
python3 -m venv myenv
```
```bash
source myenv/bin/activate
```

#### Install Required Python Packages

```bash
pip install boto3 paho-mqtt
```

---

### 5. Create and Run the Script

#### Create a Directory for the Script

```bash
mkdir ~/scripts
```
```bash
cd ~/scripts
```

#### Create the MQTT-to-S3 Script

```bash
nano mqtt_to_s3.py
```
> **Note:** Copy and paste the python code in the repo. Once done press Ctrl + X, then Y, and press Enter.

#### Run the Script

```bash
python mqtt_to_s3.py
```

---

### 6. Test MQTT to S3 Connectivity

#### Publish a Test Message

```bash
mosquitto_pub -h 51.20.85.183 -t test -m '{"DeviceID": "Device1", "Timestamp": "2025-02-06T12:00:00Z", "Data": "SampleData"}'
```
> **Note:** Check S3 bucket to ensure data is being stored.
---
