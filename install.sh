#!/bin/bash

# Colors for output
GREEN="\033[1;32m"
YELLOW="\033[1;33m"
RED="\033[1;31m"
BLUE="\033[1;34m"
RESET="\033[0m"

echo -e "${BLUE}=========================================${RESET}"
echo -e "${BLUE}       Application initialization        ${RESET}"
echo -e "${BLUE}=========================================${RESET}\n"

# Detect operating system and make some variables
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="linux"
    INSTALL_CMD="sudo apt-get install -y"
    UPDATE_CMD="sudo apt-get update"
    FFMPEG_INSTALL_CMD="sudo apt-get install -y ffmpeg"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macos"
    INSTALL_CMD="brew install"
    UPDATE_CMD="brew update"
    FFMPEG_INSTALL_CMD="brew install ffmpeg"
else
    echo -e "${RED}[ERROR] Unsupported operating system: $OSTYPE${RESET}"
    exit 1
fi

# Get script directory path
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Check python
echo -e "${YELLOW}>> Checking for Python3...${RESET}"
if ! command -v python3 &>/dev/null
then
    echo -e "${RED}Python3 not found. Installing...${RESET}"
    $UPDATE_CMD
    $INSTALL_CMD python3 python3-pip
else
    echo -e "${GREEN}Python3 is available.${RESET}"
fi

# Venv
echo -e "\n${YELLOW}>> Creating (if necessary) and activating virtual environment...${RESET}"
if [ ! -d "$DIR/venv" ]; then
    python3 -m venv "$DIR/venv"
    echo -e "${GREEN}Virtual environment created.${RESET}"
else
    echo -e "${GREEN}Virtual environment already exists.${RESET}"
fi
source "$DIR/venv/bin/activate"

# Upgrade pip
echo -e "\n${YELLOW}>> Upgrading pip...${RESET}"
pip install --upgrade pip

# Check ffmep
echo -e "\n${YELLOW}>> Checking for ffmpeg...${RESET}"
if ! command -v ffmpeg &>/dev/null
then
    echo -e "${RED}ffmpeg not found. Installing...${RESET}"
    $UPDATE_CMD
    $FFMPEG_INSTALL_CMD
else
    echo -e "${GREEN}ffmpeg is available.${RESET}"
fi

# Check python dependencies
echo -e "\n${YELLOW}>> Installing Python dependencies...${RESET}"

# Streamlit
if ! python -c "import streamlit" &>/dev/null; then
    echo -e "${RED}Streamlit not found. Installing...${RESET}"
    pip install streamlit
else
    echo -e "${GREEN}Streamlit is available.${RESET}"
fi

# PyTorch (CPU-only, universal for macOS and Linux)
if ! python -c "import torch" &>/dev/null; then
    echo -e "${RED}Torch not found. Installing...${RESET}"
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
else
    echo -e "${GREEN}Torch is available.${RESET}"
fi

# Whisper (from GitHub)
if ! python -c "import whisper" &>/dev/null; then
    echo -e "${RED}Whisper not found. Installing...${RESET}"
    pip install git+https://github.com/openai/whisper.git
else
    echo -e "${GREEN}Whisper is available.${RESET}"
fi

echo -e "\n${BLUE}=========================================${RESET}"
echo -e "${BLUE}          Installation completed!          ${RESET}"
echo -e "${BLUE}=========================================${RESET}"
