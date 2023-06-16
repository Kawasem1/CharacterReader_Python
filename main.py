import os
from PIL import Image
import pyocr

#環境変数「PATH」にTesseract-OCRのパスを設定。
path='C:\\Program Files\\Tesseract-OCR\\'
os.environ['PATH'] = os.environ['PATH'] + path
ans = []
#pyocrにTesseractを指定する。
pyocr.tesseract.TESSERACT_CMD = r'C:\\Users\prf103\Desktop\python\tesseract\tesseract.exe'
tools = pyocr.get_available_tools()
tool = tools[0]

#抽出定数
k = 50
b = 1
c = 6
#画像
for a in range(4):
    img = Image.open('C:\\Users\prf103\Desktop\python\example4.png')
    img_dtl=img.crop((k*a,0,k*b,50))
#画像の文字を抽出
    builder = pyocr.builders.TextBuilder(tesseract_layout=6)
    text = tool.image_to_string(img_dtl, lang="eng", builder=builder)
#"|"を消去しintへ変換
    text = text.replace("|","")
    int(text)
    ans.append(text)
    b+=1
print(ans)
