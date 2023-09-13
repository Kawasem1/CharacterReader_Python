def yomitori(inputPath,outputPath,name):
	import os
	from PIL import Image
	import pyocr
	from tkinter import messagebox
	path='C:\\Program Files\\Tesseract-OCR\\'
	os.environ['PATH'] = os.environ['PATH'] + path
	#回答の数、配列初期化、模範解答
	ans = []
	#pyocrにTesseractを指定する。
	pyocr.tesseract.TESSERACT_CMD = r'tesseract\tesseract.exe'
	tools = pyocr.get_available_tools()
	tool = tools[0]
	img = Image.open(inputPath)
	#画像の文字を抽出
	builder = pyocr.builders.TextBuilder(tesseract_layout=6)
	text = tool.image_to_string(img, lang="jpn", builder=builder)
	ans.append(text)
	path = os.path.join(outputPath,name) +'.txt'
	f = open(path, 'w')
	f.writelines(ans)
	f.close()
	messagebox.showinfo('読み取る君','読み取り完了！出力先:' + outputPath)
