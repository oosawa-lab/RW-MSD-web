# -----------------------------------------------------------------------------
# Copyright (c) 2025 Chikoo Oosawa, Kyushu Institute of Technology
#
# This project is licensed under the MIT License.
# You can find the full license at: https://opensource.org/licenses/MIT
#
# Repository: https://github.com/oosawa-lab/RW-MSD-web/
# -----------------------------------------------------------------------------
#
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Function to generate random walk
def generate_random_walk(steps=1000):
    x_steps = np.random.normal(0, 1, size=steps)
    y_steps = np.random.normal(0, 1, size=steps)
    x = np.cumsum(x_steps)
    y = np.cumsum(y_steps)
    return x, y

# Function to calculate the mean squared displacement (MSD)
def calculate_msd(x, y, max_lag=None):
    if max_lag is None:
        max_lag = len(x) // 2
    lags = np.arange(1, max_lag + 1)
    msd = np.zeros_like(lags, dtype=float)
    for lag in lags:
        dx = x[lag:] - x[:-lag]
        dy = y[lag:] - y[:-lag]
        msd[lag - 1] = np.mean(dx**2 + dy**2)
    return lags, msd

# Function to calculate the diffusion coefficient from MSD
def calculate_diffusion_coefficient(lags, msd):
    log_lags = np.log(lags)
    log_msd = np.log(msd)
    coeffs = np.polyfit(log_lags, log_msd, 1)
    slope = coeffs[0]
    diffusion_coefficient = np.exp(coeffs[1]) / 4
    return diffusion_coefficient, slope, coeffs

# Function to plot MSD vs Time Lag on a log-log scale
def plot_msd_loglog(lags, msd, coeffs, ax):
    ax.loglog(lags, msd, 'o-', label="MSD")
    ax.loglog(lags, np.exp(np.polyval(coeffs, np.log(lags))), 'r--', label=f"Linear Fit (Slope={coeffs[0]:.2f})")
    ax.set_xlabel("Log(Time Lag)")
    ax.set_ylabel("Log(MSD)")
    ax.set_title("MSD vs Time Lag (Log-Log Plot)")
    ax.legend()
    ax.grid(True, which="both", linestyle="--", linewidth=0.5)

# Streamlit Interface
st.title("Random Walk Simulation with Diffusion Coefficient Calculation")

# Use session_state to store steps value, initialize with default if not set
if 'steps' not in st.session_state:
    st.session_state.steps = 1000

# Create a slider to select the number of steps
steps = st.slider("Select Number of Steps:", 10, 100000, st.session_state.steps)

# Update the session state with the selected number of steps
st.session_state.steps = steps

# Create a placeholder for the plot to be updated
placeholder = st.empty()

# Function to update the plot based on selected steps
def update_plot(steps):
    x, y = generate_random_walk(steps)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    ax1.plot(x, y, marker='o', markersize=2, label="Random Walk Trajectory")
    ax1.scatter(x[0], y[0], color="green", label="Start Point", zorder=5)
    ax1.scatter(x[-1], y[-1], color="red", label="End Point", zorder=5)
    ax1.set_title("Random Walk Trajectory")
    ax1.set_xlabel("X Coordinate")
    ax1.set_ylabel("Y Coordinate")
    ax1.legend()
    ax1.grid(True)
    ax1.axis("equal")

    lags, msd = calculate_msd(x, y)
    diffusion_coefficient, slope, coeffs = calculate_diffusion_coefficient(lags, msd)
    plot_msd_loglog(lags, msd, coeffs, ax2)

    placeholder.pyplot(fig)

    # Display diffusion coefficient and slope below the plot
    st.subheader("Diffusion Coefficient and Slope")
    st.write(f"Diffusion Coefficient: {diffusion_coefficient:.2f}")
    st.write(f"Slope of Log-Log MSD Plot: {slope:.2f}")

# Initialize session state for the first time calculation
update_plot(st.session_state.steps)
