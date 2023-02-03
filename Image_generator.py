import tkinter as tk
from tkinter import ttk
import os
import openai
import requests
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

def set_openai_credentials():
    openai.organization = org_entry.get()
    openai.api_key = api_key_entry.get()

def generate_image():
    set_openai_credentials()
    global response
    response = openai.Image.create(
      prompt=keyword_entry.get(),
      n=1,
      size="1024x1024"
    )
    image_url = response['data'][0]['url']
    response = requests.get(image_url)
    with open("image.jpg", "wb") as f:
        f.write(response.content)

    image = Image.open("image.jpg")
    image = image.resize((360, 360), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo

def save_image():
    file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg"),("All Files", "*.*")])
    with open(file_path, "wb") as f:
        f.write(response.content)

def create_tab_control(root):
    tab_control = ttk.Notebook(root)
    image_gen_tab = ttk.Frame(tab_control)
    tab_control.add(image_gen_tab, text="Image Generator")
    tab_control.pack(expand=1, fill='both')
    return tab_control

root = tk.Tk()
root.title("AI image generator")
tab_control = create_tab_control(root)

org_label = tk.Label(tab_control, text="OpenAI Organization:")
org_entry = tk.Entry(tab_control)

api_key_label = tk.Label(tab_control, text="OpenAI API Key:")
api_key_entry = tk.Entry(tab_control)

keyword_label = tk.Label(tab_control, text="Keyword:")
keyword_entry = tk.Entry(tab_control)
display_button = tk.Button(tab_control, text="Generate Image", command=generate_image)
label = tk.Label(tab_control)

org_label.pack()
org_entry.pack()

api_key_label.pack()
api_key_entry.pack()

keyword_label.pack()
keyword_entry.pack()
display_button.pack()
label.pack()

save_button = tk.Button(tab_control, text="Save Image", command=save_image)
save_button.pack()

credit_label = tk.Label(tab_control, text="Author hanhg95@gmail.com - Nguyen Han")
credit_label.pack(side="bottom")

root.geometry("640x640")
root.mainloop()
