import pytesseract
from pdfplumber.page import Page

# Se estiver no Windows, aponte o caminho do executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\pedro.alcantara\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

def pdf_imageToStr(pagina:Page):
    imagem_pagina = pagina.to_image(resolution=300)
    
    # Obter a imagem no formato PIL (Python Imaging Library)
    pil_image = imagem_pagina.original
    
    # Executar o OCR na imagem
    # O parâmetro 'lang' define o idioma (ex: 'por' para português ou 'eng' para inglês <padrão>)
    texto = pytesseract.image_to_string(pil_image)
    
    return texto
