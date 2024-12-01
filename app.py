from flask import Flask, render_template
from flask_socketio import SocketIO
import paho.mqtt.client as mqtt
import app_secrets as secrets
import json
from eventlet import monkey_patch
monkey_patch()

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.APP_CONFIG
socketio = SocketIO(app, async_mode='eventlet', cors_allowed_origins="*", transports=['websocket'])


@socketio.on('connect')
def handle_connect():
    print("WebSocket client connected")
    socketio.emit('mqtt_message', {'topic': 'test', 'data': "{'hey':'ho'}"})

# MQTT callback functions
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code", rc)
    client.subscribe(secrets.MQTT_TOPIC)
    

# def on_message(client, userdata, msg):
#     decoded=json.loads(msg.payload.decode())
#     print(f"MQTT Message: {decoded}")
#     socketio.emit('mqtt_message', {'topic': msg.topic, 'data': decoded})
def on_message(client, userdata, msg):
    # decoded=json.loads()
    print(f"MQTT Message: {msg.payload.decode()}")
    socketio.emit('mqtt_message', {'topic': msg.topic, 'data': msg.payload.decode()})
    
    

# Flask route
@app.route('/')
def index():
    return render_template('index.html')


# Set up the client
client = mqtt.Client()
client.username_pw_set(secrets.MQTT_USR, secrets.MQTT_PW)
client.on_connect = on_connect
client.on_message = on_message

client.connect(secrets.MQTT_BROKER_HOST, secrets.MQTT_BROKER_PORT, 60)


client.loop_start()

# Run Flask with SocketIO
if __name__ == '__main__':
    app.debug = True
    socketio.run(app, host='0.0.0.0', port=5001, debug=True)
