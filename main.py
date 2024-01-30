import tkinter
from tkinter import ttk

import file_sys
import net_sys


file_sys.load_info()
file_sys.load_balance()
net_sys.load_icons(file_sys.info)


print(file_sys.balance)
print(file_sys.info)

print(net_sys.get_price('btc'))

window_width = 500
window_height = 500
window_x = 250
window_y = 100


window = tkinter.Tk()
window.title('investing')
window.geometry(f'{window_width}x{window_height}+{window_x}+{window_y}')
window.resizable(True, True)
window_icon = tkinter.PhotoImage(file='icons/BTC.png')
window.iconphoto(True, window_icon)


def finish():
    window.destroy()
    print('Exit application')


window.protocol('WM_DELETE_WINDOW', finish)

window.update_idletasks()

balance_frames = []
images = []
for _type in file_sys.balance:
    for asset in file_sys.balance[_type]:
        frame = ttk.Frame(window, borderwidth=1, relief=tkinter.SOLID, padding=[8, 10])

        label_type = ttk.Label(frame, text=_type)
        label_type.pack(side=tkinter.LEFT)

        if _type == 'SPOT' or _type == 'EARN':
            image = tkinter.PhotoImage(file=f'icons/{asset}.png')
            image = image
            images.append(image)
            label_image = ttk.Label(frame, image=image)
            label_image.pack(side=tkinter.LEFT)

        label_name = ttk.Label(frame, text=asset)
        label_name.pack(side=tkinter.LEFT)

        label_value = ttk.Label(frame, text=file_sys.balance[_type][asset])
        label_value.pack(side=tkinter.LEFT)

        frame.pack(anchor=tkinter.W)
        balance_frames.append(frame)

window.mainloop()
