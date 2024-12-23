# Instructions to replicate after cloning

### Ensure Python 3.9/3.10 is installed on your pc
### This program will be run on virtual environment to avoid version conflicts, so we have to set up a venv
### install cmake on your pc

### pip install virtualenv
### pip install -U average-facer

## Create a virtual environment called myenv
### python -m venv env 

## Install the dlib package
### wget http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2

## Activate the virtual environment 
### source env/bin/activate
### python -m pip install dlib

## Ensure you have selected the correct python interpreter (should be under myenv)
### Save everything
### run python main.py --> should have a popup with merged faces after some loading
