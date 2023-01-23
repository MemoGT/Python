import tkinter as tk
from tkinter import filedialog
import pandas as pd
from tabulate import tabulate

def import_csv():
    filepath = filedialog.askopenfilename()
    data = pd.read_csv(filepath)
    table = tabulate(data, headers='keys', tablefmt='grid', showindex=False)
    data_label.insert('1.0', table)

root = tk.Tk()
root.title("CSV Import")

import_button = tk.Button(text="Import CSV", command=import_csv)
import_button.grid(row=0, column=0)

data_label = tk.Text(root)
data_label.grid(row=1, column=0)
root.mainloop()

