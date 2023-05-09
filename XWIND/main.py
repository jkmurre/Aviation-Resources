from xwind import *

def main():    


    runway_heading = int(input("Runway Heading: ")) # Runway heading in degrees
    wind_speed = int(input("Wind Speed in KTS: ")) # Wind speed in knots
    wind_heading = int(input("Wind Heading: ")) # Wind heading in degrees

    crosswind = calculate_crosswind(runway_heading, wind_speed, wind_heading)
    print(f"The crosswind component is {crosswind:.2f} knots.")


if __name__ == "__main__":
    main()