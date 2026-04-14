import pdfplumber
import pandas as pd
import re
import pyperclip

from .OCR import pdf_imageToStr

coord = {
    'Processo': (r"\b(\d{5}[\/-]\d{2}[a-zA-Z])\b", r"\b(\d{4}[\/-]\d{2}[a-zA-Z])\b", r"\b(\d{5}[\/-]\d{2})\b", r"\b(\d{4}[\/-]\d{2})\b"),
    'Invoice': r"Invoice\n*(\d+)",
    'Número': r"\((\d+)\)",
    'Código': None, # definido sem utilizar o padrão regex
    'Descrição': r"Cancao fries.*x(\d)",
    'Container': r"([A-Z]{4}[-|\/_ ]?\d{6}[-|\/_ ]?\d)",
    
    'Peso': {
        'OCR': r"Value\n.*?([\d,.]{3,10})\|",
        'notOCR': r"Lacre numero[\w\s]*?\n.*? ([\d,.]*?) ",
    },
    
    'Caixas': {
        'OCR': r"Value\n.*?\|.*?\|.*?([\d.,]{1,10})",
        'notOCR': r"Quantidade de Caixas[^\d]*?([\d.,]+)\b",
    },
    
    'Valor Un.': r".*? .*? ([\d,.].*?) ", # definido com o peso concatenado com este padrão regex
    
    'Valor Total': {
        'OCR': r"Value\n.*?\|.*?\|.*?([\d.,]{4,10})\n",
        'notOCR': r"Lacre numero[\w\s]*?\n.*?([\d.,]{4,10})\n",
    },
}

def gerarLinha(filepath:str):

    data = {}

    with pdfplumber.open(filepath) as invoice:
        firstPage = invoice.pages[0]
        pageText = firstPage.extract_text()
        
        if pageText == '':
            pageText = pdf_imageToStr(firstPage)
            isOCR = 'OCR'
        else:
            isOCR = 'notOCR'
        
        for column, rePattern in coord.items():
            if rePattern != None:
                
                if column == 'Processo':
                    patterns = rePattern
                    
                    process = None
                    found = False
                    
                    for i in range(0, len(patterns), 2): # pesquisa usando padrões de dois em dois, para verificar 5 e 4 digitos de processo com letra e depois sem letra
                        
                        firstPattern = patterns[i]
                        secondPattern = patterns[i+1]
                        
                        process = re.search(firstPattern, pageText)
                        
                        if process != None:
                            data[column] = process.group(1).replace('/', '-').strip()
                            found = True
                            break
                        else:
                            process = re.search(secondPattern, pageText)
                            
                            if process != None:
                                data[column] = '0' + process.group(1).replace('/', '-').strip()
                                found = True
                                break
                    
                    if not found: 
                        data[column] = 'Não encontrado'
                
                
                elif column == 'Número':
                    invoiceIndex = re.search(rePattern, filepath, re.UNICODE)
                    
                    if invoiceIndex != None:
                        data[column] = invoiceIndex.group(1).strip()
                    else:
                        data[column] = "Sem Número"
                
                elif column == 'Descrição':
                    sizeChar = re.search(rePattern, pageText)
                    
                    if sizeChar != None:
                        sizeChar = sizeChar.group(1)
                    else:
                        sizeChar = 'Não encontrado'
                    
                    match sizeChar:
                        case '1':
                            data['Código'] = 'COMPRO000069'
                            data[column] = 'BATATA PALITO CONGELADA 9 X 9 MM PACOTE 1,1 KG CAIXA PP 9,9 KG (CANCAO ALIMENTOS)'

                        case '2':
                            data['Código'] = 'COMPRO000067'
                            data[column] = 'BATATA PALITO CONGELADA 9 X 9 MM PACOTE 2 KG CAIXA PP 10 KG (CANCAO ALIMENTOS)'

                        case '4':
                            data['Código'] = 'COMPRO000068'
                            data[column] = 'BATATA PALITO CONGELADA 9 X 9 MM PACOTE 400 G CAIXA PP 10 KG (CANCAO ALIMENTOS)'

                        case _:
                            data['Código'] = 'Não encontrado'
                            data[column] = 'Não encontrado'
                
                elif column == 'Container':
                    
                    cntr = re.search(rePattern, pageText)
                    
                    if cntr != None:
                        cntr = cntr.group(1)
                        data[column] = re.sub(r'[-|\/_ ]', '', cntr)
                    else:
                        data[column] = 'Não Encontrado'
                
                
                elif column == 'Valor Un.': # tratamento apenas depois da coluna "Peso"
                    
                        weight:str = data['Peso']
                        
                        escapedWeight = re.sub(r'(?=\.)', r'\\', weight)
                        pattern = escapedWeight + rePattern
                        
                        netPrice = re.search(pattern, pageText)
                        if netPrice != None: 
                            data[column] = netPrice.group(1)
                        else: 
                            data[column] = "Não encontrado"
                
                
                elif column == 'Peso' or column == 'Caixas' or column == 'Valor Total':
                    
                    res = re.search(rePattern[isOCR], pageText)
                    if res != None:
                        data[column] = res.group(1).strip().replace('.', '') if column == 'Caixas' else res.group(1).strip()
                    else:
                        data[column] = 'Não Encontrado'
                
                else: # casos comuns:
                    
                    res = re.search(rePattern, pageText)
                    if res != None:
                        data[column] = res.group(1).strip()
                    else:
                        data[column] = 'Não Encontrado'
                    
                    
            
    return data

def gerarRelatorio(pdf_paths:list[str]):
    data = [gerarLinha(pdf_path) for pdf_path in pdf_paths]
    df = pd.DataFrame(data)
    
    return df
