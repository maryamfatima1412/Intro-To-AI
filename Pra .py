import tkinter as tk

window = tk.Tk()
window.title("My First GUI")
window.geometry("400x250")

label = tk.Label(window, text="Hello, Python GUI!")
label.pack(pady=20)

button = tk.Button(window, text="Click Me")
button.pack()

window.mainloop()