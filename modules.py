import pdfplumber
import pandas as pd
import os
import re

coord = {
    'Processo': (136.4, 409.0, 350.9, 423.4),
    'Invoice': (83.0, 320.0, 150.0, 340.0),
    'Número': None,
    'Código': None,
    'Descrição': (55.7, 493.9, 200.1, 540.1),
    'Container': (35.4, 510, 174.2, 600.4),
    'Peso': (316.3, 494.4, 350.9, 505.4),
    'Caixas': (30.2, 494.4, 54.2, 505.4),
}

def gerarLinha(filepath:str):

    data = {}

    with pdfplumber.open(filepath) as invoice:
        firstPage = invoice.pages[0]
        
        for column, bbox in coord.items():
            
            match column:
                case 'Processo':
                    box = firstPage.within_bbox(bbox)
                    txt = box.extract_text()
                    
                    process = re.search(r'(\d{5}[\/-]\d{2})', txt)
                    
                    if process != None:
                        data[column] = process.group(1)
                    
                    else:
                        process = re.search(r'(\d{4}[\/-]\d{2})', txt)
                        
                        if process != None:
                            data[column] = '0' + process.group(1)
                            
                        else:
                            data[column] = 'Não encontrado'
                    
                    
                case 'Número':
                    invoiceIndex = re.search(r'\((\d+)\)', filepath, re.UNICODE)
                    
                    if invoiceIndex != None:
                        data[column] = invoiceIndex.group(1)
                    else:
                        data[column] = "Sem Número"
                    
                    
                case 'Código':
                    continue
                
                case 'Descrição':
                    box = firstPage.within_bbox(bbox)
                    txt = box.extract_text()
                    index = txt.find('x')
                    
                    if index != -1:
                        nextChar = txt[index+1]
                    else:
                        nextChar = None
                        txt = 'Descrição desconhecida encontrada: ' + txt
                    
                    match nextChar:
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
                            data['Código'] = 'Desconhecido'
                            data[column] = txt
                case 'Container':
                    box = firstPage.within_bbox(bbox)
                    txt = box.extract_text()
                    
                    ctnr = re.search(r'([A-Z]{4}\d{7})', txt)
                    
                    if ctnr != None:
                        data[column] = ctnr.group(1)
                    else:
                        data[column] = 'Não Encontrado'
                
                case _:
                    box = firstPage.within_bbox(bbox)
                    txt = box.extract_text()
                    data[column] = txt
    return data


def listaArquivosPdf(dir_path:str) -> list[str]:
    files = os.listdir(dir_path)
    pdf_paths = []
    
    for file in files:
        if file.endswith('.pdf') or file.endswith('.PDF'):
            pdf_path = os.path.join(dir_path, file)
            pdf_paths.append(pdf_path)
    
    return pdf_paths


def gerarRelatorio(pdf_paths:list[str], output_file:str):
    data = [gerarLinha(pdf_path) for pdf_path in pdf_paths]
    df = pd.DataFrame(data)
    
    df.to_excel(output_file, index=False)
