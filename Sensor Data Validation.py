# Sensor readings list
sensor_readings = [3, 4, 7, 8, 10, 12, 5]

# Step 1: Store valid readings
valid_readings = []

# Step 2: Loop with index
for hour, value in enumerate(sensor_readings):
    
    # Step 3: Check if even
    if value % 2 == 0:
        valid_readings.append((hour, value))

# Step 4: Display result
print("Valid Sensor Readings (Hour, Value):")
print(valid_readings)
