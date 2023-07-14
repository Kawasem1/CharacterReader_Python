# import Tkinter lib
import tkinter
# create Tkinter instance
root = tkinter.Tk()
#window title
root.title(u"読み取る君(beta)")
# windnow size w*h
root.geometry("480x250")
static1 = tkinter.Label(text=u'読み取る画像のパスを入力してください',font=('',12))
static1.place(x=10,y=10)
editbox = tkinter.Entry(width=50)
editbox.place(x=10,y=30)

def pathRead(event):
    path = editbox.get()
    print(path)
    
button = tkinter.Button(text=u'読み取る')
button.place(x=210,y=220)
button.bind("<Button-1>",pathRead)

filesansyo = tkinter.Button(text=u'ファイル選択')
filesansyo.place(x=320,y=27)
def sansyo(event):
    from tkinter import filedialog
    typ = [('画像ファイル','*.png')]
    fle = filedialog.askopenfilename(filetypes = typ, initialdir = dir)
    editbox.insert(tkinter.END,fle)
filesansyo.bind("<Button-1>",sansyo)

root.mainloop()
