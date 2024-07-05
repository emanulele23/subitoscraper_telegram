import subprocess
import glob
import time
import os

# Installa i pacchetti da requirements.txt al primo avvio
if not os.path.exists('requirements_installed.txt'):
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
    with open('requirements_installed.txt', 'w') as f:
        f.write('')

# Ottieni una lista di tutti i file .py nella directory corrente
script_files = glob.glob('*.py')

# Rimuovi il file 'main.py' dalla lista, se presente
script_files.remove('main.py')

while True:
    # Esegui add_item.py ogni 10 minuti
    subprocess.run(['python', '/home/raspi/Desktop/Scraper2_Bot/create_new_scraping_item/add_item.py'])
    time.sleep(600)  # Attendiamo 10 minuti

    # Esegui gli altri script ogni 3 minuti
    for script in script_files:
        subprocess.run(['python', script])
        time.sleep(180)  # Attendiamo 3 minuti

