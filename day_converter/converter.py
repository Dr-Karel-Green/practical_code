# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 14:38:59 2025
README: Code that converts a number of days into how many years/months that 
corresponds to 
@author: uazkg2
"""
#%% Modules
import PyInstaller
import datetime as dt
import tkinter as tk

#%% Functions

def days_to_ymd(total_days):
    default_date = dt.date(1, 1, 1) #choosing 1st Jan 0001 as a starting date
    
    new_date = default_date + dt.timedelta(days=total_days)
    
    yrs = new_date.year - default_date.year
    mth = new_date.month - default_date.month
    day = new_date.day - default_date.day
    
    yrs_label  = "year"   if yrs  == 1 else "years"
    mths_label = "month"  if mth == 1 else "months"
    day_label   = "day"    if day   == 1 else "days"
    
    str1 = f"{total_days} days is:"
    str2 = f"{yrs} {yrs_label}, {mth} {mths_label} and {day} {day_label}"
    return(str1, str2)
 
    
#%% Making interface
root = tk.Tk()

#%%Window title and dimensions
root.geometry('350x200') #widthxheight of window

root.title("Days to years converter")
#%% Label and button
lbl = tk.Label(root, text = "Input number of days:")
lbl.grid()

# adding Entry Field
txt = tk.Entry(root, width=10)
txt.grid(column=1, row=0, padx=5, pady=5, sticky="w")

# adding the button
btn = tk.Button(root, text = "Convert", fg = "red", command=days_to_ymd)
btn.grid(column=2, row=0, padx=5, pady=5)

#%% Calls function when button is clicked

def on_click(event=None):
    try:
        num_days = int(txt.get())
        str1, str2 = days_to_ymd(num_days)
        result_lbl.config(text=f"{str1}\n{str2}")
    except ValueError:
        result_lbl.config(test='Please enter a valid number')

btn.config(command=on_click)

#%% Printing output to the window of the function

result_lbl = tk.Label(root, text="", justify='left', anchor='w')
result_lbl.grid(column=0, row=1, columnspan=3, padx=5, pady=10, sticky='w')


root.bind('<Return>', on_click)

#%%Running the applicaiotn
root.mainloop()
#%% save as exe
#pyinstaller --onefile --windowed converter.py [write that in the terminal]
