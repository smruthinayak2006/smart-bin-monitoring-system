# Smart Waste Management System 🚮

A simple smart waste bin prototype built using Arduino and an ultrasonic sensor to monitor bin fill level and trigger alerts when the bin is getting full.

## Problem
Bins often overflow because there is no real-time indication of fill level.

This prototype demonstrates how low-cost sensors can help monitor waste levels and alert authorities before overflow happens.

---

## Features
- Fill level detection using ultrasonic sensor  
- Green LED for normal state  
- Red LED for warning state  
- Buzzer alert for overflow  
- Three-state monitoring logic:
  - Normal
  - Warning
  - Overflow

---

## Components Used
- Arduino Uno  
- HC-SR04 Ultrasonic Sensor  
- 2 LEDs (Green and Red)  
- Piezo Buzzer  
- 220Ω Resistors  
- Breadboard + Jumper Wires

---

## Working Logic

Distance-based monitoring:

```text
> 20 cm   → Normal (Green LED)

10–20 cm  → Warning (Red LED)

< 10 cm   → Overflow (Red LED + Buzzer)
```

---

## Prototype Validation Results

### Normal State
![Normal](images/bin-normal.png)

---

### Warning State
![Warning](images/bin-warning.png)

---

### Overflow Alert
![Overflow](images/bin-overflow.png)

---

## Circuit Overview

```text
Ultrasonic Sensor
   ↓
Arduino Uno
   ↓
Status Alerts
(LEDs + Buzzer)
```

---

## Project Structure

```text
smart-waste-management-iot/
├── firmware/
├── hardware/
├── images/
├── docs/
└── README.md
```

---

## How It Works
The ultrasonic sensor measures the distance from the sensor to the garbage level.

Distance is used to determine whether the bin is:
- Empty/Normal
- Near Full
- Overflowing

Alerts are triggered automatically based on threshold values.

---

## Future Improvements
Planned upgrades:
- IoT dashboard monitoring
- Smart pickup alerts
- Route optimization for collection vehicles
- Fill-level prediction

---

## Tech Used
- Arduino C/C++
- Tinkercad Simulation
- Git + GitHub

---

## Why I Built This
This project was built as a small smart-city/IoT prototype to explore sensor-based automation and waste monitoring.

---

## Author
Smruthi Nayak  
BTech CSE (IoT)

