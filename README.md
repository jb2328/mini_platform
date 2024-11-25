# Mini Platform

A lightweight platform integrating Flask, Socket.IO, and MQTT for real-time messaging between web clients and an MQTT broker.

## Features

- **Flask**: Backend web framework.
- **Flask-SocketIO**: Real-time WebSocket communication.
- **Paho MQTT**: MQTT client integration for subscribing and publishing messages.
- **HTML Frontend**: Simple frontend to log messages in real time.

## Project Structure

- `app.py`: Main Flask application
- `app_secrets.py`: Secrets configuration (excluded from Git)
- `templates/index.html`: Frontend HTML
- `venv/`: Virtual environment (excluded from Git)
- `.gitignore`: Git ignore file

## Requirements

- Python 3.9+
- MQTT Broker (e.g., Mosquitto)
- Flask-SocketIO
- Paho MQTT
- Eventlet


## Installation

1. **Clone the Repository**:
   bash  
   git clone https://github.com/jb2328/mini_platform.git  
   cd mini_platform  
   

2. **Set Up Virtual Environment**:
python3 -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate  

3. **Install Dependencies**:

pip install -r requirements.txt

4. **Run**:

python app.py
Open http://127.0.0.1:5001 in your browser.  

