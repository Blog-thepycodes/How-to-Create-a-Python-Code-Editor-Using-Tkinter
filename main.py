import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
import subprocess
 
 
# Initialize the file path
file_path = ''
 
 
def set_file_path(path):
   global file_path
   file_path = path
 
 
def open_code():
   path = askopenfilename(filetypes=[('Python Files', '*.py')])
   if path:
       with open(path, 'r') as file:
           code = file.read()
           code_input.delete('1.0', tk.END)
           code_input.insert('1.0', code)
           set_file_path(path)
 
 
def save_code():
   global file_path
   if not file_path:
       file_path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
 
 
   if file_path:
       with open(file_path, 'w') as file:
           code = code_input.get('1.0', tk.END)
           file.write(code)
 
 
def run_code():
   global file_path
   if not file_path:
       messagebox.showerror("Python IDE", "Please save your code before running.")
       return
 
   command = f'python {file_path}'
   process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
   output, error = process.communicate()
   code_output.delete('1.0', tk.END)
   code_output.insert('1.0', output.decode())
   code_output.insert('1.0', error.decode())
 
 
# Create the main window
root = tk.Tk()
root.title("Python IDE - The Pycodes")
root.geometry("800x600")
 
# Create a text widget for code input
code_input = tk.Text(root, font=("Courier New", 14))
code_input.pack(fill=tk.BOTH, expand=True)
 
# Create a text widget for code output
code_output = tk.Text(root, font=("Courier New", 14))
code_output.pack(fill=tk.BOTH, expand=True)
 
# Create buttons for Open, Save, and Run
open_button = tk.Button(root, text="Open", command=open_code)
save_button = tk.Button(root, text="Save", command=save_code)
run_button = tk.Button(root, text="Run", command=run_code)
 
open_button.place(x=30,y=520)
save_button.place(x=300,y=520)
run_button.place(x=600,y=520)
 
 
root.mainloop()
