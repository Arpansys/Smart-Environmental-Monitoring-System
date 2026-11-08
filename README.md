# Smart Environmental Monitoring and Alert System

An Arduino-based environmental monitoring and alert system integrated with a Python multi-agent architecture and Google Gemini AI for intelligent fault detection, system analysis, and automated troubleshooting.

## 1. Project Overview

The Smart Environmental Monitoring and Alert System monitors environmental conditions using multiple sensors connected to an Arduino Uno.

The system measures temperature, humidity, and gas sensor readings. When abnormal conditions or sensor faults are detected, the Arduino activates visual warning indicators and communicates sensor data to a Python-based multi-agent system.

The Python agents analyse incoming data, validate sensor readings, identify possible faults, and generate debugging recommendations. Google Gemini AI is integrated to provide additional intelligent fault diagnosis when the system detects a test failure.

## 2. Key Features

- Real-time temperature and humidity monitoring.
- Gas sensor monitoring.
- 16x2 I2C LCD for displaying sensor information.
- Red and green LED indicators for warning and normal conditions.
- Touch-based alert acknowledgement using TTP223.
- Automatic detection of DHT11 sensor faults.
- Serial communication between Arduino and Python.
- Four-agent Python architecture for system analysis and debugging.
- Gemini AI-powered fault diagnosis and recommendations.
- Fault recovery detection when normal sensor operation resumes.

## 3. Hardware Requirements

| Component | Purpose |
|---|---|
| Arduino Uno | Main hardware controller |
| DHT11 | Temperature and humidity measurement |
| FC-22 Gas Sensor | Gas detection |
| 16x2 I2C LCD | Sensor readings and warning display |
| TTP223 Touch Sensor | Alert acknowledgement and display switching |
| Red LED | Warning indication |
| Green LED | Normal operation indication |
| Jumper wires | Hardware connections |
| USB cable | Power and serial communication |

## 4. Hardware Connections

| Component | Arduino Pin |
|---|---|
| DHT11 Data | D10 |
| FC-22 Analog Output | A0 |
| TTP223 Signal | D3 |
| Green LED | D4 |
| Red LED | D6 |
| LCD SDA | A4 |
| LCD SCL | A5 |

The LCD uses I2C address `0x27`.

**Note:** The gas sensor reading is currently represented as a raw analog value (0–1023), not a calibrated gas concentration in ppm.

## 5. Software Requirements

- Python 3
- Arduino IDE
- PyCharm (recommended)
- Git
- Google Gemini API key

### Python Dependencies

Install the required packages using:

```bash
pip install pyserial python-dotenv google-genai
```

### Arduino Libraries

Install the libraries required by your Arduino sketch, including:

- DHT sensor library
- Adafruit Unified Sensor (if required by the DHT library)
- LiquidCrystal_I2C

## 6. Software Architecture

The system consists of an Arduino monitoring unit and a Python-based multi-agent architecture.

### Arduino Monitoring Unit

The Arduino reads sensor values, evaluates warning conditions, controls the LEDs, updates the LCD, and sends data to the Python application through serial communication.

### Python Multi-Agent System

The project contains four specialised agents:

**Agent 1 – System Architect (`system_architect.py`)**

Analyses the overall system structure and evaluates the system configuration.

**Agent 2 – Embedded Programmer (`embedded_programmer.py`)**

Analyses the embedded system and firmware-related information.

**Agent 3 – Test Engineer (`test_engineer.py`)**

Validates incoming sensor readings, checks acceptable ranges, and evaluates warning conditions.

**Agent 4 – Debugging Engineer (`debugging_engineer.py`)**

Analyses the reports from the other agents, identifies possible problems, and provides debugging recommendations.

### Gemini AI Integration (`ai_assistant.py`)

Google Gemini AI provides an additional diagnostic layer.

When the Python system detects a test failure, the application can send the relevant diagnostic information to Gemini for:

- Identification of possible faults.
- Analysis of likely causes.
- Suggested corrective actions.
- Verification recommendations.

Gemini is called only when a failure is detected, helping avoid unnecessary API requests.

## 7. Project Structure

```text
Smart-Environmental-Monitoring-System/
│
├── main.py
├── ai_assistant.py
├── system_architect.py
├── embedded_programmer.py
├── test_engineer.py
├── debugging_engineer.py
├── arduino_test.py
├── README.md
├── .gitignore
│
└── Arduino/
    └── Environmental_Monitoring.ino
```

The Arduino folder name and sketch filename are illustrative; use the actual names in your repository.

## 8. Configuration

### Gemini API Configuration

1. Obtain a Gemini API key from Google AI Studio.
2. Create a file named `.env` in the project root.
3. Add the following:

```env
GEMINI_API_KEY=your_api_key_here
```

4. Save the file.

**Important:** Never upload your `.env` file or expose your API key on GitHub.

### Serial Port Configuration

Open `main.py` and configure the serial port to match your Arduino connection.

For example:

```python
PORT = "COM3"
BAUD_RATE = 9600
```

Change the COM port if your Arduino uses a different one.

Close the Arduino IDE Serial Monitor before running the Python application because only one application should access the serial port at a time.

## 9. How to Run the Project

1. Connect the Arduino Uno to your computer.
2. Open the Arduino sketch in Arduino IDE.
3. Upload the firmware to the Arduino.
4. Close the Arduino Serial Monitor.
5. Install the required Python dependencies.
6. Configure the Gemini API key in `.env`.
7. Verify the serial port configuration in `main.py`.
8. Run the Python application:

```bash
python main.py
```

The Python application will receive sensor readings, execute the agents, display diagnostic reports, and request Gemini analysis when required.

## 10. Testing and Validation

The following tests can be performed to demonstrate system functionality.

| Test | Expected Result |
|---|---|
| Normal sensor operation | Valid readings and green LED |
| LCD display switching | Touch sensor switches display information |
| Gas warning condition | Red LED warning and LCD alert |
| Alert acknowledgement | Serial output confirms acknowledgement |
| DHT11 disconnection | Sensor fault detected and warning activated |
| Python fault simulation | Agents identify invalid sensor readings |
| Gemini diagnosis | AI provides possible causes and recommendations |
| Sensor reconnection | System returns to normal operation |

**Note:** Python-only fault simulation does not physically change the Arduino sensor readings or LED states.

## 11. Warning Thresholds

The current firmware uses the following temperature and gas warning thresholds:

| Parameter | Warning Threshold | Clear Threshold |
|---|---:|---:|
| Temperature | 35°C | 33°C |
| Gas Sensor Raw Reading | 70 | 60 |

Hysteresis is used to prevent repeated switching between warning and normal states near the threshold.

These values are configurable in the Arduino firmware.

## 12. Future Improvements

Potential future improvements include:

- Gas sensor calibration for concentration estimation.
- Cloud-based environmental data storage.
- Web-based monitoring dashboard.
- Historical sensor data visualisation.
- Additional environmental sensors.
- Mobile notifications for critical alerts.
- Automated system recovery and reporting.

## 13. Technologies Used

- Arduino Uno
- Embedded C/C++ (Arduino)
- Python
- Multi-Agent Architecture
- Google Gemini API
- PySerial
- python-dotenv
- Git and GitHub

## 14. Author

Developed as an academic project demonstrating embedded systems, environmental monitoring, Python multi-agent architecture, and AI-assisted fault diagnosis.

---

**Smart Environmental Monitoring and Alert System**

*Combining embedded hardware, intelligent software agents, and generative AI for environmental monitoring and fault diagnosis.*
