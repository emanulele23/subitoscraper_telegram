import gspread
from oauth2client.service_account import ServiceAccountCredentials
from jinja2 import Template
import os

# Configura le credenziali per accedere a Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
# Assicurati di avere il file JSON delle credenziali nella stessa directory del tuo script
creds = ServiceAccountCredentials.from_json_keyfile_name('bot-telegram-subito-b323c3e65a33.json', scope)
client = gspread.authorize(creds)

# Apri il foglio di calcolo
spreadsheet = client.open('Bot Telegram Scraping Subito (Responses)')
worksheet = spreadsheet.get_worksheet(0)  # Sostituisci con l'indice del foglio di calcolo desiderato

# Leggi i dati dal foglio di calcolo
data = worksheet.get_all_records()

# Ottieni il percorso completo del file template
template_path = '/home/pi/Scraper0_Bot/templates/python_template.py'

# Verifica se il file template esiste
if not os.path.exists(template_path):
    print(f"Template file not found at {template_path}. Please make sure it exists.")
    exit(1)

# Carica il tuo template da un file
with open(template_path, 'r') as template_file:
    template_content = template_file.read()

# Usa Jinja2 per creare il nuovo file basato sul template
template = Template(template_content)

# Crea una directory 'execution_folder' se non esiste
execution_folder = '/home/pi/Scraper0_Bot/execution_folder'
if not os.path.exists(execution_folder):
    os.makedirs(execution_folder)

# Itera sulle righe dei dati e crea file Python personalizzati
for row in data:
    file_name = row['File Name']
    link = row['Link']

    if file_name and link:
        # Sostituisci il segnaposto {{ LINK }} con il link dal foglio di calcolo
        template_content_with_link = template_content.replace('{{ LINK }}', link)
        # Scrivi il contenuto nel nuovo file solo se non esiste già
        output_file_path = f'{execution_folder}/{file_name}.py'
        if not os.path.exists(output_file_path):
            with open(output_file_path, 'w') as new_file:
                new_file.write(template_content_with_link)
                print(f"Created file: {output_file_path}")

print("Files created successfully.")
