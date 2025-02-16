# RW-MSD-web
Random Walk and Diffusion Coefficient Calculator - Web Application

This repository contains a web-based implementation of a random walk simulation that calculates the diffusion coefficient and mean squared displacement (MSD) using Streamlit.
Users can control the number of steps in the random walk, visualize the trajectory, and see how the diffusion coefficient behaves as a function of the MSD.

Features

Random Walk Simulation: Generate and visualize a 2D random walk trajectory based on a specified number of steps.
Mean Squared Displacement (MSD): Compute the MSD as a function of the time lag and visualize it on a log-log scale.
Diffusion Coefficient Calculation: Estimate the diffusion coefficient from the slope of the MSD vs. time lag plot.
Interactive Controls: Use a slider to adjust the number of steps and view the corresponding results in real-time.
Visualization: View both the random walk trajectory and MSD plot side by side.
Requirements

To run this project, you'll need the following Python libraries:

numpy
matplotlib
streamlit

How It Works

Random Walk Generation: The app generates a random walk trajectory by taking steps that follow a normal distribution.
The user can adjust the number of steps through a slider.
MSD Calculation: The Mean Squared Displacement (MSD) is calculated by comparing the positions of the walk at different time lags.
It is then plotted against the time lag on a log-log scale.
Diffusion Coefficient: The diffusion coefficient is estimated from the slope of the log-log MSD plot, which represents the relationship between MSD and time lag in a 2D random walk.

Usage

Use the slider to select the number of steps for the random walk.
The random walk trajectory will be displayed on the left.
The log-log MSD plot will be shown on the right.
The app automatically calculates and displays the diffusion coefficient and slope of the MSD plot.
