from tkinter import *
from xwind import *

'''

Makes up the Tkinter GUI file. 

Includes widgets and labels for the runway heading, wind speed, and wind heading, as well as a result label, submit button and reset button. 

'''

class GUI:
    def __init__(self, window):

        '''
        
        Initialize GUI instance.

        
        Args: Tkinter window object.

        Returns: None
        
        '''

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
        self.frame_submit_button = Frame(self.window)
        self.label_crosswind = Label(self.window, text="")
        self.label_crosswind.pack(pady=10)

        # Submit button
        self.frame_submit_button = Frame(self.window)
        self.button_submit = Button(self.window, text="Submit", command=self.submitted)
        self.button_submit.pack(pady=10)

        # Reset button
        self.frame_reset_button = Frame(self.window)
        self.button_reset = Button(self.window, text="Reset", command=self.reset)
        self.button_reset.pack(pady=10)

        # Set initial focus 
        self.entry_runway_heading.focus()

    def submitted(self):

        '''
        
        Executes the calculate_crosswind function from xwind.py when the user clicks it and then updates the result label. 

        Returns: None

        '''
        try:
            # Get values
            runway_heading = float(self.entry_runway_heading.get())
            wind_speed = float(self.entry_wind_speed.get())
            wind_heading = float(self.entry_wind_heading.get())
            
            if not (0 <= runway_heading < 360) or wind_speed < 0 or not (0 <= wind_heading < 360):
                raise ValueError("Invalid input")

            # Calculate crosswind component 
            crosswind = calculate_crosswind(runway_heading, wind_speed, wind_heading)

            # Update the label with the crosswind component 
            self.label_crosswind.config(text=f"The crosswind component is {crosswind:.2f} knots.")
            
        except ValueError as e:
            self.label_crosswind.config(text=str(e))
            
    def reset(self):
        '''

        Executes when the user clicks the Reset button. It clears the entries and the crosswind 
        component label.

        Returns: None

        '''

        # Clear the text fields
        self.entry_runway_heading.delete(0,END)
        self.entry_wind_heading.delete(0,END)
        self.entry_wind_speed.delete(0,END)

        # Clear the result label
        self.label_crosswind.config(text="")
