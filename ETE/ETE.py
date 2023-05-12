import math

# TODO: Add docstring and type hinting where needed.
# TODO: Isolate appropriate parts to a dedicated function and add if __name__ call.

# Get user input for departure winds and validate input
departure_winds = input("Enter departure winds in the format 'ddd@ss': ")
try:
    departure_wind_direction, departure_wind_speed = departure_winds.split("@")
    departure_wind_direction = int(departure_wind_direction)
    departure_wind_speed = int(departure_wind_speed)
except ValueError:
    print("Error: Invalid input format for departure winds. Please enter in the format 'ddd@ss'.")
    exit()

# Get user input for destination winds and validate input
destination_winds = input("Enter destination winds in the format 'ddd@ss': ")
try:
    destination_wind_direction, destination_wind_speed = destination_winds.split("@")
    destination_wind_direction = int(destination_wind_direction)
    destination_wind_speed = int(destination_wind_speed)
except ValueError:
    print("Error: Invalid input format for destination winds. Please enter in the format 'ddd@ss'.")
    exit()

# Get user input for distance and validate input
distance_input = input("Enter distance between airports in nautical miles: ")
try:
    distance = float(distance_input)
except ValueError:
    print("Error: Invalid input for distance. Please enter a number.")
    exit()

# Get user input for airspeed and validate input
airspeed_input = input("Enter airspeed in knots: ")
try:
    airspeed = float(airspeed_input)
except ValueError:
    print("Error: Invalid input for airspeed. Please enter a number.")
    exit()

# Calculate wind correction angle and ground speed
heading = math.atan2(destination_wind_speed * math.sin(math.radians(destination_wind_direction - departure_wind_direction)), (airspeed + departure_wind_speed * math.cos(math.radians(destination_wind_direction - departure_wind_direction))))
ground_speed = (airspeed + departure_wind_speed * math.cos(math.radians(destination_wind_direction - departure_wind_direction))) * math.cos(heading) - destination_wind_speed * math.sin(math.radians(destination_wind_direction - departure_wind_direction))

# Calculate estimated time enroute
time_enroute = distance / ground_speed

# Output result
print("Estimated time enroute: ", round(time_enroute, 2), "hours")
