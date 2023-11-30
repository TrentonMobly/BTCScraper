import csv
import re

def trova_indirizzi_btc(file_csv, colonna_testo):
    indirizzi_btc = set()

    with open(file_csv, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for riga in reader:
            testo = riga[colonna_testo]
            indirizzi_trovati = re.findall(r'\b[13][a-km-zA-HJ-NP-Z1-9]{25,34}\b', testo)

            indirizzi_btc.update(indirizzi_trovati)

    return indirizzi_btc

# Esempio di utilizzo:
file_csv_input = ''
colonna_testo_input = ''

indirizzi_trovati = trova_indirizzi_btc(file_csv_input, colonna_testo_input)

print("Indirizzi BTC trovati:")
for indirizzo in indirizzi_trovati:
    print(indirizzo)
