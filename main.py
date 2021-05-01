import requests
import time
import tkinter as tk
import concurrent.futures
import os
import getpass

# getpass to get current username
# path variable to store Download Location
user_name = getpass.getuser()
path = fr"C:\Users\{user_name}\Downloads"

root = tk.Tk()
root.geometry('400x200')
root.title("ImgDownloader")
url_var = tk.StringVar()


def down():
    '''
    This function uses the given url to download the image from the server
    '''
    url = url_var.get()
    print(f'{url}')
    img_byt = requests.get(url).content
    img_name = url.split('/')[-1]
    img_name = img_name.split('.')[0]
    img_name = f'{img_name}.jpg'
    nam = os.path.join(path, img_name)
    with open(nam, 'wb') as img_file:
        img_file.write(img_byt)
        print(f'{img_name} was downloaded.....')


# Label for Url

ded = tk.Label(root, text='Enter Url :').place(x=40, y=60)

# Entry for url
inp = tk.Entry(root, width=40, textvariable=url_var).place(x=110, y=60)

# Button For Download

check = tk.Button(root, text="Download", width='25', command=down).place(x=90, y=100)

# Label for Download path

ded = tk.Label(root, text=f'The Download Location is \n {path}').place(x=90, y=130)


root.mainloop()
