import os
from PIL import Image
import pyocr

#環境変数「PATH」にTesseract-OCRのパスを設定。
path='C:\\Program Files\\Tesseract-OCR\\'
os.environ['PATH'] = os.environ['PATH'] + path
#回答の数、配列初期化、模範解答
e_cnt = 10
ans = []
ans_t=[3,4,3,4,3,4,5,5,6,7]
#pyocrにTesseractを指定する。
pyocr.tesseract.TESSERACT_CMD = r'.\tesseract\tesseract.exe'
tools = pyocr.get_available_tools()
tool = tools[0]

#抽出定数
k = 50
b = 1
c = 6
#画像
for a in range(e_cnt):
    img = Image.open('.\example4.png')
    img_dtl=img.crop((k*a,0,k*b,50))
#画像の文字を抽出
    builder = pyocr.builders.TextBuilder(tesseract_layout=6)
    text = tool.image_to_string(img_dtl, lang="eng", builder=builder)
#"|"を消去しintへ変換
    text = text.replace("|","")
    text =int(text)
    ans.append(text)
    b+=1
#答え合わせ
d = 0
for d in range(e_cnt):
    if ans[d] == ans_t[d]:
        print(f'Q{d+1} 正解!')
    else:
        print(f'Q{d+1} 不正解 => A.{ans_t[d]}')
print(ans)
