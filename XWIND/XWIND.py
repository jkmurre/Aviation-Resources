import math

    # TODO: Make a GUI.
    # TODO: Isolate function and add if __name__ call. 

def calculate_crosswind(runway_heading: float, wind_speed: float, wind_heading: float) -> float:
    """
    Calculates the crosswind component given the runway heading, wind speed, and wind heading.

    Args:
    - runway_heading (float): The runway heading in degrees.
    - wind_speed (float): The wind speed in knots.
    - wind_heading (float): The wind heading in degrees.

    Returns:
    - crosswind (float): The crosswind component in knots.

    Example usage:
    runway_heading = int(input("Runway Heading: "))
    wind_speed = int(input("Wind Speed in KTS: "))
    wind_heading = int(input("Wind Heading: "))
    crosswind = calculate_crosswind(runway_heading, wind_speed, wind_heading)
    print(f"The crosswind component is {crosswind:.2f} knots.")
    """
    # Convert the runway heading and wind heading from degrees to radians
    runway_heading = math.radians(runway_heading)
    wind_heading = math.radians(wind_heading)

    # Calculate the angle between the runway heading and wind heading
    angle = wind_heading - runway_heading

    # Calculate the crosswind component using the wind speed and the angle
    crosswind = math.sin(angle) * wind_speed

    return crosswind

# Example usage
runway_heading = int(input("Runway Heading: ")) # Runway heading in degrees
wind_speed = int(input("Wind Speed in KTS: ")) # Wind speed in knots
wind_heading = int(input("Wind Heading: ")) # Wind heading in degrees

crosswind = calculate_crosswind(runway_heading, wind_speed, wind_heading)
print(f"The crosswind component is {crosswind:.2f} knots.")
