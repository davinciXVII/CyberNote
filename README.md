# davinciXVII - CyberNote v2.0 🚀

A high-tech, Cyberpunk-themed desktop text editor built with Python and Tkinter. This lightweight application provides a distraction-free writing environment combined with automated background features.

## 🌟 Key Features
* **Asynchronous Auto-Save Engine:** Automatically backs up your text every 5 seconds without freezing the UI (built via `window.after` loops).
* **Live Status Bar:** Tracks word and character counts in real-time utilizing asynchronous event binding (`<KeyRelease>`).
* **Native File System Integration:** Seamlessly open, create, and "Save As" text documents using Python's `os` and `filedialog` modules.
* **Cyberpunk Dark Theme:** Designed with customized visual markers and an active neon hacker green cursor for comfortable night coding/writing.

## 🛠️ Tech Stack & Concepts Used
* **Language:** Python 3
* **GUI Framework:** Tkinter (Menus, Cascades, Text, Labels, Checkbuttons)
* **File Handling:** Built-in I/O operations with robust `utf-8` encoding.
* **Error Handling:** Safe execution architecture (`try/except`) for image/asset loading and environment tracking.
