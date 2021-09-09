from tkinter import Label, Tk
import time
app_window = Tk()
app_window.title("My Digital Time")
app_window.geometry("1535x900")
app_window.resizable(0,0)
text_font = ("Boulder", 250, 'bold')
background = "#000000"
foreground= "#E0E1E4"
border_width = 100
label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)
def digital_clock():
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live)
   label.after(200, digital_clock)
digital_clock()
app_window.mainloop()