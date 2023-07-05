import os
from PIL import Image
import pyocr

#環境変数「PATH」にTesseract-OCRのパスを設定。
path='C:\\Program Files\\Tesseract-OCR\\'
os.environ['PATH'] = os.environ['PATH'] + path
#回答の数、配列初期化、模範解答
ans = []
#pyocrにTesseractを指定する。
pyocr.tesseract.TESSERACT_CMD = r'..\tesseract\tesseract.exe'
tools = pyocr.get_available_tools()
tool = tools[0]
img = Image.open('..\読み取りdata\利用者データ-1.png')
#画像の文字を抽出
builder = pyocr.builders.TextBuilder(tesseract_layout=6)
text = tool.image_to_string(img, lang="jpn", builder=builder)
table = str.maketrans('ま', '*')
text.translate(table)
ans.append(text)

f = open('..\kore.txt', 'w')
f.writelines(ans)
f.close()
