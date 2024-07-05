import bs4
import requests
import time
import telegram
import json
import os

# Ottieni il nome del file Python in esecuzione senza l'estensione '.py'
file_name = os.path.splitext(os.path.basename(__file__))[0]

LINK = "{{ LINK }}"  # Questo è il segnaposto per il link da sostituire
PRELINK = "https://www.subito.it/"
TOKEN = "5951805607:AAEjx1ASFcWYhpAGUCNVJB5GVKBVgyJe3fk"
chat_id = '-1002064088819'

def check(LINK, PRELINK, TOKEN, chat_id):
    response = requests.get(LINK)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    # to be checked 1
    div_annunci = soup.find('div', class_='ListingContainer_col__1TZpb ListingContainer_items__3lMdo col items')

    # to be checked 2
    a_annunci = div_annunci.find_all('a')
    link_annunci = []

    for a_annuncio in a_annunci:
        link_annuncio = str(a_annuncio.get('href'))
        if PRELINK in link_annuncio:
            link_annunci.append(link_annuncio)

    # Crea il nome del file di salvataggio con il formato desiderato
    save_file_name = f'links_{file_name}.txt'

    f = open(save_file_name, 'a')  # edit2
    old_links = [riga.rstrip('\n') for riga in open(save_file_name)]  # edit3
    new_links = []

    for link_annuncio in link_annunci:
        if link_annuncio not in old_links:
            new_links.append(link_annuncio)
            f.write('%s\n' % link_annuncio)

    f.close()

    if new_links:
        print('Nuovi annunci! Invio messaggio in corso...')

        # Personalizza il messaggio basato sul nome del file .py
        custom_message = f'Nuovo annuncio "{file_name.replace("_", " ").title()}"!'

        for new_link in new_links:
            message = f"{custom_message}\n{new_link}"
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
            print(requests.get(url).json())

    else:
        no_new_announcement_message = f'Nessun nuovo annuncio "{file_name.replace("_", " ").title()}"'
        print(no_new_announcement_message)

    # time.sleep(15)

# In questo punto, dovresti avere il segnaposto {{ LINK }} per il link.

# Verifica che LINK venga passato come argomento a questa funzione check()
check(LINK, PRELINK, TOKEN, chat_id)  # edit
