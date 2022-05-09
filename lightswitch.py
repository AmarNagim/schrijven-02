import tkinter as tk
import logging

filePath = '/Users/amarnagim/Library/CloudStorage/OneDrive-DaVinciCollege/Da Vinci College/software_developen/Assignments/jaar_1/periode_1/fase_1/09_data.files.state.save/schrijven-02/actions.log'

with open(filePath, 'w'):
    pass

logging.basicConfig(filename=filePath, level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
window = tk.Tk()

print('De lamp is uit..')


# schijf hier tussen je code
window.configure (background="black")
currentState = 'off'
# currentStateSwitch = True

# while currentStateSwitch == True:

text = 'off'
def onclick():
    logging.debug('Knop geklikt')
    global currentState
    if currentState == 'on':
        button['text'] = 'Switch light on'
        print('De lamp is uit..')
        logging.debug('De lamp is uit')
        window.configure (background="black")
        currentState = 'off' 
    elif currentState == 'off':   
        button['text'] = 'Switch light off'
        print('De lamp is aan..')
        logging.debug('De lamp is aan')
        window.configure (background="yellow")
        currentState = 'on'  
                    
button = tk.Button(text=f'Switch light on', fg="black", command=onclick)
button.pack(pady = 20, padx = 20)


# schijf hier tussen je code

window.mainloop()