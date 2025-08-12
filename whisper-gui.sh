#!/bin/bash

# Retrieve the path directory of the script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Activate the virtual environment
source "$DIR"/venv/bin/activate

echo "Launch Streamlit app : "
python3 -m streamlit run "$DIR"/app.py --server.maxUploadSize=1024