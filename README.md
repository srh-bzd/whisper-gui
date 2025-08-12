# Whisper-GUI

A Streamlit app that uses OpenAI's Whisper model to transcribe audio.

<img width="1590" height="883" alt="Capture d’écran du 2025-08-12 18-02-01" src="https://github.com/user-attachments/assets/e4379103-0c3a-42f5-851a-1b42e51717b1" />



## Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Uninstall](#uninstall)
- [Notes](#notes)
- [License](#license)



## About

In fields like journalism and anthropology, transcription is part of the job — and anyone who’s done it knows how much time it eats up. Doing it by hand is slow and repetitive.

There are now great tools to make the job easier, like [OpenAI’s Whisper](https://github.com/openai/whisper). It’s powerful and supports many languages, but for people who aren’t used to working with command lines, getting it set up can be a headache.

That’s why I built Whisper-GUI. It’s a simple, point-and-click interface for Whisper. You just upload your audio, pick your settings, and get a transcription or translation right in your browser. No coding, only one command in the terminal.

To make setup even easier, the project includes an auto-installation script for Linux and macOS.



## Features

- **User-friendly** — clean Streamlit interface, no coding required
- **One-command setup** — bash script installs Python dependencies, ffmpeg, and Whisper automatically (Linux/macOS)
- **Multiple Whisper models** — choose from lightweight (tiny) to high-accuracy (large)
- **Multilingual support** — transcribe in 90+ languages or use auto-detection
- **Translation** — convert non-English speech into English text
- **Model caching** — speeds up repeated transcriptions
- **Local transcription** — all audio processing happens on your machine; no files are uploaded to the internet, ensuring privacy
- **Downloadable results** — save transcriptions as `.txt` files
- **Wide file format support** — works with `.mp3`, `.wav`, `.mp4`, `.m4a`, and more



## Installation

**1. Clone the repository**

- Command-line :

```bash
git clone https://github.com/srh-bzd/whisper-gui.git
```

- or point-and-click :

Into the repository, click on <img width="116" height="44" alt="Capture d’écran du 2025-08-12 16-25-11" src="https://github.com/user-attachments/assets/85dc3193-d9f5-4f77-9e9b-5abdf38f95fd" /> button, then <img width="137" height="44" alt="Capture d’écran du 2025-08-12 16-27-45" src="https://github.com/user-attachments/assets/cf264a71-809f-446d-a8ac-9f60062b0f26" />.

- Once the .zip file has been downloaded, unzip it.

**2. Install prerequisites and dependencies**

- Open a terminal 

- Execute the `install.sh` script

  - Intermediate way :

  ```bash
  cd whisper-gui*
  bash install.sh
  ```

  - Easy way :
    - Drag and drop the `install.sh` file into your terminal window
    - Move the cursor to the beginning of the line and type `bash ` (make sure there is a space after `bash`)
    - Press Enter

- The installation will be complete when you see the following in the terminal:

```
=========================================
          Installation completed!          
=========================================
```



## Usage

**Launch the app**

- Open a terminal 

- Execute the `whisper-gui.sh` script

  - Intermediate way :

  ```bash
  cd whisper-gui*
  bash whisper-gui.sh
  ```

  - Easy way :
    - Drag and drop the `whisper-gui.sh` file into your terminal window
    - Move the cursor to the beginning of the line and type `bash ` (with a trailing space)
    - Press Enter

- Your local browser will open with the app.

**Close the app**

- Simply close the terminal window to stop the app.



## Uninstall

To uninstall Whisper-GUI, simply delete the project directory. This will remove the app and all its files, including the virtual environment. There’s no additional uninstall script or process needed.



## Notes

- The **app** and its virtual environment take up about **2 GB of disk space** on your computer 
- Some of the Whisper **models** (especially the bigger ones : turbo and large) can use a **lot of RAM** while running
- By "**word**" we mean any **group of characters delimited by spaces**. So, even a question mark "?" counts as a word here
- The **turbo** model will return the **original language even if translate** is specified



## License

This project is licensed under the MIT License.

