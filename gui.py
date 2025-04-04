from pathlib import Path
import json
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar, filedialog, messagebox
# import shutil, os # I inted to make config.json has temporary backup.
# Import the process_deck function from process.py
from process import process_deck

# Current Script DIR (where gui.py is)
OUTPUT_PATH = Path(__file__).parent
CONFIG_PATH = "config.json"
# Relative Path to assets
ASSETS_RELATIVE_PATH = Path("assets")

# Absolute path for relative path assets
ASSETS_PATH = OUTPUT_PATH / ASSETS_RELATIVE_PATH

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def save_entry_4():
    with open(CONFIG_PATH, 'w') as f:
        f.write(entry_4.get("1.0", "end-1c"))
        
# Specify PDF
def pickPDF():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    Input_PDF.set(file_path)
# Specify folder output
def pickFolder():
    folder_path = filedialog.askdirectory()
    Output_Path.set(folder_path)

window = Tk()

Input_PDF = StringVar()
Output_Path = StringVar()
Deck_Name = StringVar()
Config = StringVar()

# Check whether all the variables pass the requirements for Deck Creation?
def isPass(): 
    def isValidFile(file_path):
        return file_path.endswith('.pdf')

    def isValidPath(folder_path):
        return Path(folder_path).is_dir()

    def isValidJSON(json_path):
        try:
            with open(json_path, 'r') as f:
                json.load(f)
            return True, None
        except json.JSONDecodeError as e:
            return False, e

    isInput_PDF = Input_PDF.get()
    isOutput_Path = Output_Path.get()
    isConfig = CONFIG_PATH
    isDeck_Name = Deck_Name.get()

    if not isInput_PDF:
        messagebox.showwarning("Warning", "Input path is empty.")
        return False, None
    if not isValidFile(isInput_PDF):
        messagebox.showwarning("Warning", "Input path is not a valid PDF file. Ensure that it ends with \'.pdf\' extension. Look out for typo too.")
        return False, None

    if not isOutput_Path:
        messagebox.showwarning("Warning", "Output folder path is empty. ")
        return False, None
    if not isValidPath(isOutput_Path):
        messagebox.showwarning("Warning", "Output path is not a valid folder. Ensure that it is a folder, not a file extension. Look out for typo too.")
        return False, None

    if not isDeck_Name:
        messagebox.showwarning("Warning", "Deck name is empty.")
        return False, None

    if not Path(isConfig).exists():
        messagebox.showwarning("Warning", "Config JSON file does not exist.")
        return False, None
    valid, error = isValidJSON(isConfig)
    if not valid:
        messagebox.showwarning("Warning", f"Config JSON is invalid: {error}\nEnsure that there is no typo in JSON.\nIf you are lost, use \'config-backup.json\'")
        return False, None

    # Call fn:process_deck of process.py
    result = process_deck(isInput_PDF, isOutput_Path, isDeck_Name)
    messagebox.showinfo("Result", f"Process completed: {result}")
    
    return (isInput_PDF, isOutput_Path, isDeck_Name)

window.geometry("362x415")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 415,
    width = 362,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    362.0,
    415.0,
    fill="#000000",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    184.0,
    253.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    184.0,
    197.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    184.0,
    138.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    184.0,
    78.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    184.0,
    330.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    183.0,
    106.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    183.0,
    163.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    183.0,
    220.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    181.0,
    30.0,
    image=image_image_9
)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: isPass(),
    relief="flat"
)

button_1.place(
    x=252.0,
    y=10.0,
    width=99.0,
    height=34.0
)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    182.0,
    106.5,
    image=entry_image_1
)

entry_1 = Entry(
    bd=0,
    bg="#181818",
    fg="#FFFFFF",
    font=("Arial", 10),
    highlightthickness=0,
    textvariable=Input_PDF
)
entry_1.bind("<Button-1>", lambda event: pickPDF())
entry_1.place(
    x=62.0,
    y=97.0,
    width=240.0,
    height=17.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    182.0,
    163.5,
    image=entry_image_2
)

entry_2 = Entry(
    bd=0,
    bg="#181818",
    fg="#FFFFFF",
    font=("Arial", 10),
    highlightthickness=0,
    textvariable=Output_Path
)
entry_2.bind("<Button-1>", lambda event: pickFolder())
entry_2.place(
    x=62.0,
    y=154.0,
    width=240.0,
    height=17.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    182.0,
    220.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#181818",
    fg="#FFFFFF",
    font=("Arial", 10),
    highlightthickness=0,
    textvariable=Deck_Name
)
entry_3.place(
    x=62.0,
    y=211.0,
    width=240.0,
    height=17.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
     184.0,
    329.0,
    image=entry_image_4
)
entry_4 = Text(
    bd=0,
    bg="#181818",
    fg="#181818", 
    font=("Arial", 7),
    highlightthickness=0
)
entry_4.place(
    x=60.0,
    y=273.0,
    width=248.0,
    height=110.0
)
# Load config upon start
with open(CONFIG_PATH, 'r') as f:
    entry_4.insert("1.0", f.read())
# Saves config upon release
entry_4.bind("<KeyRelease>", lambda event: window.after(1000, save_entry_4))
# Just to ensure no one sees it.
entry_4.bind("<Enter>", lambda event: entry_4.config(fg="#FFFFFF"))
entry_4.bind("<Leave>", lambda event: entry_4.config(fg="#181818"))

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    48.0,
    404.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    330.0,
    403.0,
    image=image_image_11
)
window.resizable(False, False)
window.mainloop()
