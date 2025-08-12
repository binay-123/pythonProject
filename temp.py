import numpy as np

# Temperature in Celsius
temp_cel = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])

# 1. Calculate and print average temperature
avg_temp = np.mean(temp_cel)
print(f"Average temperature (°C): {avg_temp:.2f}")

# 2. Determine and display highest and lowest temperatures
highest_temp = np.max(temp_cel)
lowest_temp = np.min(temp_cel)
print(f"Highest temperature (°C): {highest_temp}")
print(f"Lowest temperature (°C): {lowest_temp}")

# 3. Convert all temperatures to Fahrenheit
temp_f = temp_cel * 9/5 + 32
print("Temperatures in Fahrenheit:", temps_f)

# 4. Identify and print indices of days with temp > 20°C
indices_above_20 = np.where(temp_cel > 20)[0]
print("Indices of days with temperature > 20°C:", indices_above_20)