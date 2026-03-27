import pdfplumber

coord = {
    'Processo': (136.4, 409.0, 217.9, 423.4),
    'Invoice': (83.0, 320.0, 150.0, 340.0),
    'Número': None,
    'Código': None,
    'Descrição': (55.7, 493.9, 214.1, 530.1),
    'Container': (121.4, 521.3, 174.2, 531.4),
    'Peso': (316.3, 494.4, 350.9, 505.4),
    'Caixas': (30.2, 494.4, 54.2, 505.4),
}


def lastInParentesis(str):
    start = None
    end = None
    
    for i in range(len(str) -1, 0, -1):
        if str[i] == ')':
            end = i

        elif str[i] == '(':
            start = i + 1
            
    if start == None or end == None:
        return None
    else:
        return str[start:end]

def gerarLinha(filepath):

    data = {}

    with pdfplumber.open(filepath) as invoice:
        firstPage = invoice.pages[0]
        
        for column, bbox in coord.items():
            
            match column:
                case 'Processo':
                    box = firstPage.within_bbox(bbox)
                    txt = box.extract_text()
                    index = txt.find('-')
                    
                    if index == -1:
                        process = txt
                            
                    else:
                        process = txt[index+1:]
                        
                    if process[0] == '0':
                        data[column] = process
                    else:
                        data[column] = '0' + process
                    
                case 'Número':
                    invoiceIndex = lastInParentesis(filepath)
                    
                    try:
                        int(invoiceIndex)
                    except ValueError and TypeError:
                        invoiceIndex = "Sem Número"
                    
                    data[column] = invoiceIndex
                    
                    
                    
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
                
                case _:
                    box = firstPage.within_bbox(bbox)
                    txt = box.extract_text()
                    data[column] = txt
    return data