#  Snap Automation Launcher

A real-time gesture-triggered automation system that launches development tools using a **finger snap**.

---

##  Overview

This project uses **microphone input + signal processing** to detect a snap sound and trigger a workflow that opens:

* VS Code
* Google Chrome
* Antigravity AI IDE

Think of it as a **mini Jarvis system** for developers.

---

##  How It Works

1. Continuously listens to microphone input
2. Measures sound amplitude in real-time
3. Detects a sharp spike (snap)
4. Triggers system commands to launch applications
5. Uses a **lock mechanism** to prevent multiple triggers

---

##  Core Concept

> Edge-triggered impulse detection with a refractory lock to ensure single-event execution from multi-peak audio signals.

---

##  Tech Stack

* Python
* sounddevice (real-time audio input)
* numpy (signal processing)
* subprocess (system automation)

---

##  Project Structure

```
snap-automation/
│
├── snap_launcher.py
└── requirements.txt
```

---

##  Installation

```bash
pip install sounddevice numpy
```

---

##  Run

```bash
python snap_launcher.py
```

---

##  Usage

* Run the script
* Snap your fingers near the microphone
* Watch your dev environment launch instantly ⚡

---

##  Configuration

Inside `snap_launcher.py`:

```python
THRESHOLD = 0.15     # sensitivity
LOCK_TIME = 1.5      # cooldown duration
```

Adjust based on your microphone sensitivity.

---

##  Notes

* Ensure microphone permissions are enabled
* Works best in a quiet environment
* Threshold tuning may be required per device

---

##  Features

* Real-time audio processing
* Snap detection using amplitude spikes
* Multi-app automation
* Debounced triggering (no repeated launches)

---

##  Future Improvements

* Snap vs clap classification (ML-based)
* Background service (runs on startup)
* Custom workflow configuration
* GUI dashboard
* Voice + gesture hybrid control

---

## 💡 Inspiration

Inspired by the idea of creating a **gesture-controlled developer assistant**, similar to systems seen in sci-fi interfaces aka Mr. Tony Stark - The Iron-Man

---

## 🧾 One-Line Summary

> A gesture-driven automation system that uses real-time audio signal processing to trigger developer workflows.

---


