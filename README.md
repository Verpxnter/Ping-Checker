# Ping-Checker

Ping-Checker is a robust, real-time web application designed to monitor and visualize network ping statistics, providing an intuitive way to track network latency and performance. By offering live updates every second, Ping-Checker helps users stay informed about their network's health, enabling quick response to any issues.

## Features

- **Real-Time Monitoring**: Continuously updates to show the latest network ping in milliseconds, providing an accurate, up-to-the-second picture of network latency.
- **Dynamic Line Chart**: Displays ping data as a line chart, which automatically adjusts its y-axis based on the highest observed values, providing a clear view of trends and fluctuations.
- **Color-Coded Status**: Ping quality is color-coded (e.g., green for optimal, red for high latency), allowing for quick assessment of network conditions at a glance.
- **Comprehensive Statistics**: Displays current, highest, and lowest ping values, providing an overall view of network performance over time.
- **Responsive and Adaptable Design**: The chart resizes based on the browser window, offering a seamless viewing experience on different devices.

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/verpxnter/ping-checker.git
    cd ping-checker
    ```

2. **Install required dependencies:**
    Ensure Python and pip are installed, then run:
    ```bash
    pip install -r requirements.txt
    ```

3. **Adjust file permissions:**
    Give execution rights to the necessary scripts:
    ```bash
    sudo chmod +x run.sh run.py
    ```

4. **Run the application:**
    Start the server by executing:
    ```bash
    sudo ./run.sh
    ```

5. **Access the application in your browser:**
    Replace `<YOUR-IP>` with your server's IP address:
    ```
    http://<YOUR-IP>:1234/
    ```

## Usage

- **Current Ping**: Displays the most recent ping result, helping you gauge immediate network status.
- **Highest/Lowest Ping**: Keeps a record of the maximum and minimum ping values seen since the application started, providing insight into peak latency times.
- **Ping Trend Chart**: A dynamic, real-time line chart displays a history of ping values, with each point showing its respective timestamp when hovered over.

## Technologies Used

- **HTML/CSS/JavaScript**: For a clean, responsive front-end interface.
- **Chart.js**: A powerful charting library used to create the real-time ping trend chart.
- **Date-fns**: A lightweight date formatting library, simplifying date manipulation for timestamped data.

## Customization

- **Fetch Interval**: By default, Ping-Checker fetches new data every second. To modify this interval, update the `setInterval` value in the JavaScript section of `index.html`.
- **Chart Options**: The chart’s y-axis can be further customized to refine the displayed range or adjust tick intervals, providing flexibility for different monitoring needs.

## Troubleshooting & Support

- **Permissions Issue**: If you encounter permissions errors, ensure the `chmod` command has been applied correctly, and check that `run.sh` and `run.py` have the proper executable permissions.
- **Network Accessibility**: If you can’t access the application via IP, check firewall settings to allow traffic on port 1234, or try accessing it from a device within the same network.

---

Enjoy a streamlined, real-time approach to network monitoring with Ping-Checker, and stay informed about your network’s performance!
