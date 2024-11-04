from flask import Flask, render_template, jsonify
import os
import subprocess
import time
import json
import requests
from threading import Thread

# LOCAL_IP = "google.com"       # Tests with google Server
LOCAL_IP = "192.168.178.1"      # Test with local Network (Router)
HIGH_PING_THRESHOLD = 50        # Define whats the High-Ping
DISCORD_WEBHOOK_URL = "<Your Webhook URL>"
LOG_FILE = './ping_log.csv'     # Define the Logfile
PING_INTERVAL = 3600            # Define the Ping Interval (For Webhook Notification)
REAL_TIME_PING_INTERVAL = 1     # Define the Ping Interval (For the Website)

latest_ping_data = {
    "timestamp": "",
    "ping_time": 0,
    "highest_ping": {"time": "", "value": 0},
    "lowest_ping": {"time": "", "value": float('inf')}
}

app = Flask(__name__)       

def send_to_discord(message):       # Send Messages to an discord Webhook
    payload = json.dumps({"content": f"{message}"})
    headers = {"Content-Type": "application/json"}
    requests.post(DISCORD_WEBHOOK_URL, data=payload, headers=headers)  

def ping_test():        # Pings the LOCAL_IP
    global internet_state, high_ping_detected, latest_ping_data

    while True:
        try:
            ping_result = subprocess.run(
                ["ping", "-c", "1", LOCAL_IP],
                capture_output=True,
                text=True
            )
            ping_status = ping_result.returncode

            if ping_status == 0:
                ping_time = float(ping_result.stdout.split('time=')[-1].split(' ms')[0])
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

                latest_ping_data["timestamp"] = timestamp
                latest_ping_data["ping_time"] = ping_time

                if ping_time > latest_ping_data["highest_ping"]["value"]:
                    latest_ping_data["highest_ping"]["value"] = ping_time
                    latest_ping_data["highest_ping"]["time"] = timestamp

                if ping_time < latest_ping_data["lowest_ping"]["value"]:
                    latest_ping_data["lowest_ping"]["value"] = ping_time
                    latest_ping_data["lowest_ping"]["time"] = timestamp

                with open(LOG_FILE, 'a') as log_file:
                    log_file.write(f"{timestamp},{ping_time}\n")

                if ping_time > HIGH_PING_THRESHOLD:
                    if not high_ping_detected:
                        send_to_discord(f"Warning! High ping detected: {ping_time}ms")
                        high_ping_detected = True
                else:
                    high_ping_detected = False

                if internet_state == "offline":
                    send_to_discord("Reconnected to the Local Network!")
                    internet_state = "online"
            else:
                if internet_state == "online":
                    send_to_discord("Warning! The connection is lost.")
                    internet_state = "offline"

        except Exception as e:
            print(f"Error during ping test: {e}")

        time.sleep(REAL_TIME_PING_INTERVAL)

@app.route('/') # Loads the page
def index():
    return render_template('index.html')

@app.route('/ping')     # To Access the request from js
def ping():
    return jsonify(latest_ping_data)

if __name__ == '__main__':
    internet_state = "online"
    high_ping_detected = False

    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'w') as log_file:
            log_file.write("timestamp,ping_time\n")

    ping_thread = Thread(target=ping_test, daemon=True)
    ping_thread.start()

    app.run(host='0.0.0.0', port=1234, debug=True)
