import pandas as pd
import os

from modules import *

dir_path = './Leitor de Invoices'

if not os.path.exists(dir_path):
    os.mkdir(dir_path)

files = os.listdir(dir_path)

data = []

for file in files:
    if file.endswith('.pdf'):
        
        file_path = os.path.join(dir_path, file)
        data.append(gerarLinha(file_path))
        

df = pd.DataFrame(data)

df.to_excel("Relatório.xlsx", index=False)