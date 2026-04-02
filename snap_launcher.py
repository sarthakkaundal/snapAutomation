import sounddevice as sd
import numpy as np
import os
import time
import subprocess

# ===== CONFIG =====
THRESHOLD = 0.15     # snap detection level
RESET_LEVEL = 0.05   # when sound drops below this → ready again
COOLDOWN = 2         # seconds between triggers

last_trigger = 0
triggered = False

# ===== ACTION =====
def launch_apps():
    subprocess.Popen("code")                          # VS Code
    subprocess.Popen("start chrome", shell=True)      # Chrome
    subprocess.Popen("antigravity", shell = True)

# ===== AUDIO CALLBACK =====
LOCK_TIME = 1.5   # seconds to completely ignore input after trigger
lock_until = 0

def callback(indata, frames, time_info, status):
    global last_trigger, triggered, lock_until

    volume = np.max(np.abs(indata)) * 100
    print(volume)

    now = time.time()

    # HARD LOCK (ignore everything during this time)
    if now < lock_until:
        return

    if volume > THRESHOLD:
        print("Snap detected ⚡")
        launch_apps()

        # activate hard lock
        lock_until = now + LOCK_TIME

# ===== MAIN LOOP =====
print("Listening... Press Ctrl+C to stop")

try:
    with sd.InputStream(callback=callback):
        while True:
            time.sleep(0.1)
except KeyboardInterrupt:
    print("\nStopped cleanly.")