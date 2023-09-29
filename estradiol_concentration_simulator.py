import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('tkagg')

# Constants
gel_mass = 5  # g
estradiol_concentration = 0.6  # mg/g
bioavailability = 0.1  # 10%
blood_volume = 3.5432  # L
half_life = 37.0  # hours
dose_interval = 24.0  # hours
days = 15

# Convert units
blood_volume_ml = blood_volume * 1000  # L to ml
estradiol_dose_micrograms = gel_mass * estradiol_concentration * bioavailability * 1000  # mg to ug

# Calculate decay constant from half-life
decay_constant = np.log(2) / half_life

# Initialize variables
time_hours = np.arange(0, days*24, 1)  # time in hours
estradiol_concentration_pg_ml = np.zeros_like(time_hours, dtype=float)  # concentration in pg/ml

# Simulate over time
for i, t in enumerate(time_hours):
    # Decay concentration over time (if not the first hour)
    if i > 0:
        dt = time_hours[i] - time_hours[i-1]
        estradiol_concentration_pg_ml[i] = estradiol_concentration_pg_ml[i-1] * np.exp(-decay_constant * dt)

    # Add dose
    if t % dose_interval == 0:
        estradiol_concentration_pg_ml[i] += estradiol_dose_micrograms * (1e6 / blood_volume_ml)  # ug to pg

# Print results
for t, c in zip(time_hours, estradiol_concentration_pg_ml):
    #print(f"Time: {t} hours, Estradiol concentration: {c/1000} pg/ml")
    print(f"{t} h, {c/1000} pg/ml")

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(time_hours, estradiol_concentration_pg_ml/1000, label='Estradiol concentration')
plt.xlabel('Time (hours)')
plt.ylabel('Estradiol concentration (pg/ml)')
plt.title('Estradiol concentration over time')
plt.legend()
plt.grid(True)
plt.show()
