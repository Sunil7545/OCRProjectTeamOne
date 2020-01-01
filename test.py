try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
# pytesseract.pytesseract.tesseract_cmd
# import PyPDF2
# from pdf2image import convert_from_path

def ocer_core(inputImage):
    text = pytesseract.image_to_string(inputImage)
    return text

fileName = 'shweta.jpg' # file taken from Akriti
inputData = Image.open(fileName)
textData = ocer_core(inputData)
print(type(inputData),type(textData))
# data=open('img2txt.txt','w+')
# data.write(textData)
# data.close()
rawData = textData.splitlines()
indices = [idx for idx, value in enumerate(rawData) if 'Name' in value] # data indices consisting of names
data = [rawData[i] for i in indices]
