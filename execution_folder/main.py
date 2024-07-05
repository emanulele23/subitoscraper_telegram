import subprocess
import glob
import time
import os

# Installa i pacchetti da requirements.txt al primo avvio
#if not os.path.exists('requirements_installed.txt'):
#    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
#    with open('requirements_installed.txt', 'w') as f:
#        f.write('')

while True:
    # Ottieni una lista di tutti i file .py nella directory corrente
    script_files = glob.glob('*.py')

    # Rimuovi il file 'main.py' dalla lista, se presente
    script_files = [script for script in script_files if script != 'main.py']

    for script in script_files:
        subprocess.run(['python', script])
    
    time.sleep(180)  # Attendiamo 3 minuti prima della prossima iterazione

