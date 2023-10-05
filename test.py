#Import the required Libraries
import library as database
from tkinter import *
from tkinter import messagebox

def extract_data():
    print(text_box.get('1.0', 'end'))


ws = Tk()
ws.title('PythonGuides')
ws.geometry('800x300')
ws.config(bg='#84BF04')


message ='''
You are invited to a Birthday Party

venue: Az Resort
Timing: 7 pm, wednesday

Please visit with family.

Regards,
James


'''

text_box = Text(
    ws,
    height=2,
    width=10,
    wrap='word'
)
text_box.pack(expand=True)
text_box.insert('end', message)

Button(
    ws,
    text='Change Text',
    command=extract_data
).pack(expand=True)
message2 ='''
You are invited to a Birthday Party

venue: Az Resort
Timing: 7 pm, wednesday

Please visit with family.


'''

text_box2 = Text(
    ws,
    height=2,
    width=10,
    wrap='word'
)
text_box2.pack(expand=True, side = LEFT )
text_box2.insert('end', message2)

Button2(
    ws,
    text='Change Text',
    command=extract_data
).pack(expand=True)
ws.mainloop()