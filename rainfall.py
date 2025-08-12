import numpy as np

# Sample rainfall data (mm)
rainfall_list = [0.1, 5.2, 3.0, 0.0, 13.8, 0.0, 8.5]

# 1. Convert list to NumPy array
rainfall = np.array(rainfall_list)
print("Rainfall data (mm):", rainfall)

# 2. Total rainfall for the week
total_rainfall = np.sum(rainfall)
print(f"Total rainfall for the week: {total_rainfall:.1f} mm")

# 3. Average rainfall for the week
avg_rainfall = np.mean(rainfall)
print(f"Average rainfall for the week: {avg_rainfall:.2f} mm")

# 4. Count days with no rain
no_rain_days = np.sum(rainfall == 0)
print(f"Number of days with no rain: {no_rain_days}")

# 5. Days (indices) with rainfall > 5 mm
days_above_5mm = np.where(rainfall > 5)[0]
print("Days with rainfall > 5 mm (indices):", days_above_5mm)

# 6. 75th percentile of rainfall
percentile_75 = np.percentile(rainfall, 75)
print(f"75th percentile of rainfall: {percentile_75:.2f} mm")

# 7. Values above the 75th percentile
above_75th = rainfall[rainfall > percentile_75]
print("Rainfall values above 75th percentile:", above_75th)