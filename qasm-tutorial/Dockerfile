# Docker container with IBM's Quantum Information Software Development Kit  

FROM jupyter/base-notebook:latest
#FROM python:latest

RUN pip install qiskit
COPY qiskit-tutorial-master /home/jovyan/ 
COPY Qconfig.py /home/jovyan/qiskit-tutorial-master/
