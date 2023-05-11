from tkinter import *
from xwind import *

class GUI:
    def __init__(self, window):
        # Size and init window 
        self.window = window 

        # Create frame for the runway heading widget
        self.frame_runway_heading = Frame(self.window)
        self.label_runway_heading = Label(self.frame_runway_heading, text="Runway Heading")
        self.entry_runway_heading = Entry(self.frame_runway_heading)
        self.label_runway_heading.pack(padx=5, side='left')
        self.entry_runway_heading.pack(padx=5, side='left')
        self.frame_runway_heading.pack(anchor='w', pady=10)

        # Create frame for wind speed widget
        self.frame_wind_speed = Frame(self.window)
        self.label_wind_speed = Label(self.frame_wind_speed, text="Wind Speed")
        self.entry_wind_speed = Entry(self.frame_wind_speed)
        self.label_wind_speed.pack(padx=5, side='left')
        self.entry_wind_speed.pack(padx=5, side='left')
        self.frame_wind_speed.pack(anchor='w', pady=10)

        # Create frame and widget for wind heading 
        self.frame_wind_heading = Frame(self.window)
        self.label_wind_heading = Label(self.frame_wind_heading, text="Wind Heading")
        self.entry_wind_heading = Entry(self.frame_wind_heading)
        self.label_wind_heading.pack(padx=5, side='left')
        self.entry_wind_heading.pack(padx=5, side='left')
        self.frame_wind_heading.pack(anchor='w', pady=10)

        # Create label for the crosswind component 
        self.label_crosswind = Label(self.window, text="")
        self.label_crosswind.pack(pady=10)

        # Submit button
        self.button_submit = Button(self.window, text="Submit", command=self.submitted)
        self.button_submit.pack(pady=10)

        # Set initial focus 
        self.entry_runway_heading.focus()

    def submitted(self):
        # Get values
        runway_heading = float(self.entry_runway_heading.get())
        wind_speed = float(self.entry_wind_speed.get())
        wind_heading = float(self.entry_wind_heading.get())

        # Calculate crosswind component 
        crosswind = calculate_crosswind(runway_heading, wind_speed, wind_heading)

        # Update the label with the crosswind component 
        self.label_crosswind.config(text=f"The crosswind component is {crosswind:.2f} knots.")
