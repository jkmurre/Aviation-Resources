from gui import *

# TODO: Make GUI

def main():    

    window = Tk()
    window.title('Crosswind Component Calculator')
    window.geometry('400x230')
    window.resizable(False,False)

    GUI(window)
    window.mainloop()

if __name__ == "__main__":
    main()