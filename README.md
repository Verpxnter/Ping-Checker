# Ping-Checker

Ping-Checker is a real-time web application that monitors and visualizes network ping statistics. It provides an intuitive interface to track network latency, updating every second to help you stay on top of network performance.

## Features

- **Real-Time Monitoring**: Displays current, highest, and lowest ping times in milliseconds.
- **Dynamic Chart**: A live-updating line chart visualizes ping trends, automatically adjusting the y-axis scale based on observed values.
- **Color-Coded Status**: Different colors indicate the ping quality (e.g., green for low latency, red for high), allowing for quick status assessment.
- **Statistics at a Glance**: Instant access to current, highest, and lowest recorded ping times for quick analysis.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/verpxnter/ping-checker.git
    cd ping-checker
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Add the rights:
    ```bash
    sudo chmod +x run.sh run.py
    ```

4. Run the file:
    ```bash
    sudo ./run.sh
    ```

4. Open the application in your browser:
    ```
    http://<UR-IP>:1234/
    ```

## Usage

- **Current Ping**: Displays the latest ping in milliseconds.
- **Highest/Lowest Ping**: Shows the maximum and minimum ping values recorded since the app started.
- **Ping Chart**: A live-updating line chart displays ping values over time, with tooltips showing timestamps.

## Technologies Used

- **HTML/CSS/JavaScript**: For the front-end and visual components.
- **Chart.js**: Used to create dynamic, responsive charts.
- **Date-fns**: For easy date formatting.

## Customization

To change the ping fetch interval or chart settings, adjust the values in the JavaScript section of `index.html`.

---

Enjoy monitoring your network performance with Ping-Checker!
