#!/bin/bash

# Create the Conda environment
echo "Creating the Conda environment..."
conda create -n llm_flask python=3.11 -y

# Initialize Conda for bash shell, adjust this if using a different shell
source ~/miniconda3/etc/profile.d/conda.sh

# Activate the environment
echo "Activating the environment..."
conda activate llm_flask

# Install packages
echo "Installing the LLaMA C++ Python bindings"
export CMAKE_ARGS="-DLLAMA_CUBLAS=on"
pip install llama-cpp-python

echo "Installing other Python requirements from requirements.txt..."
pip install -r requirements.txt

echo "Setup complete!"
