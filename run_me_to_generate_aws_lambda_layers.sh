#!/bin/bash
# Read.md --creates Lambda layers, Make sure to update below variable 'Layer_name' based on package names

Layer_name='pip_requests_layer'

# Install zip utility if not already installed
sudo yum install -y zip

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate
pip install boto3

# Create a directory for the SDK layer and move into it
mkdir latest-sdk-layer
cd latest-sdk-layer

# Install dependencies in the target directory specified by the virtual environment
pip3 install -qU -r ../requirements.txt -t python/lib/python3.12/site-packages/

# Package the installed dependencies into a zip file
zip -rq latest-sdk-layer.zip .

# Move back to the original directory and run additional Python script if needed
cd ..
python3 packages.py "$Layer_name"

# Deactivate the virtual environment
deactivate
