from gui import *


def main() -> NONE:  
    '''

    Launches the Crosswind Calculator GUI Application

    Returns: None

    '''

    # Create new Tkinter object and set the window title 
    window = Tk()
    window.title('Crosswind Component Calculator')

    # Size window and disable re-sizing
    window.geometry('400x400')
    window.resizable(False,False)

    # Call GUI class and loop
    GUI(window)
    window.mainloop()

if __name__ == "__main__":
    main()