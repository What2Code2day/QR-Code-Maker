from tkinter import *
from tkinter import ttk
import qrcode
import random
root = Tk()
root.title("QR Code Maker")
def create_code():
    # Link for website
    linknum = random.randint(1,100)
    link_make= 'qrcode'+ str(linknum)+'.png'
    user_link = link_entry.get()
    
    #Creating an instance of qrcode
    qr = qrcode.QRCode(
            box_size=12,
            border=5)
    qr.add_data(user_link)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(link_make)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

link = StringVar()
link_entry = ttk.Entry(mainframe, width=7, textvariable=link)
link_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Button(mainframe, text="Make QR Code", command=create_code).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Enter Link").grid(column=3, row=1, sticky=W)

link_entry.focus()
root.bind("<Return>", create_code)
root.mainloop()
