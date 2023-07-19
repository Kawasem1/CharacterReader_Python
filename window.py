# import Tkinter lib
import tkinter
# create Tkinter instance
root = tkinter.Tk()
#window title
root.title(u"読み取る君(beta)")
# windnow size w*h
root.geometry("480x250")
#ファイル読み取り処理
static1 = tkinter.Label(text=u'読み取る画像のパスを入力してください')
static1.place(x=10,y=10)
editbox = tkinter.Entry(width=50)
editbox.place(x=10,y=30)

def Read(event):
    from tkinter import messagebox
    inputPath = editbox.get()
    if len(inputPath) == 0 :
        messagebox.showerror('読み取る君', '読み取りファイルパスが未入力です。')
    outputPath = editbox2.get()
    if len(outputPath) == 0 :
        messagebox.showerror('読み取る君', '出力先ファイルパスが未入力です。')
    print(inputPath,outputPath)
    import os
    name = os.path.splitext(os.path.basename(inputPath))[0]
    import main
    main.yomitori(inputPath,outputPath,name)
    
button = tkinter.Button(text=u'読み取る')
button.place(x=210,y=220)
button.bind("<Button-1>",Read)

filesansyo = tkinter.Button(text=u'参照')
filesansyo.place(x=320,y=27)

def sansyo(event):
    from tkinter import filedialog
    typ = [('画像ファイル','*.png')]
    fle = filedialog.askopenfilename(filetypes = typ, initialdir = dir)
    editbox.insert(tkinter.END,fle)
filesansyo.bind("<Button-1>",sansyo)

#出力ファイル読み取り処理
static2 = tkinter.Label(text=u'出力ファイルの保存先を指定してください。')
static2.place(x=10,y=50)
editbox2 = tkinter.Entry(width=50)
editbox2.place(x=10,y=70)
outputFlie = tkinter.Button(text=u'参照')
outputFlie.place(x=320,y=67)

def pathRead2(event):
    from tkinter import messagebox

    print(outputPath)

def foldersansyo(event):
    from tkinter import filedialog
    fld = filedialog.askdirectory(initialdir = dir) 
    editbox2.insert(tkinter.END,fld)
outputFlie.bind("<Button-1>",foldersansyo)

root.mainloop()
