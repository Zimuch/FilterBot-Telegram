# FilterBot
Italiano

## Introduzione
**FilterBot** è un bot progettato per monitorare i messaggi in canali pubblici di Telegram alla ricerca di parole chiave specifiche. Quando viene rilevata una corrispondenza, il bot invia una notifica all'utente con un link diretto al messaggio originale.

Il progetto nasce dall'esigenza di non perdere offerte, annunci o discussioni rilevanti all'interno di canali ad alto volume di messaggi. Invece di dover controllare manualmente più canali, questo bot automatizza il processo filtrando solo i contenuti che corrispondono ai tuoi interessi specifici.

L'approccio è semplice ma efficace: il bot si connette a Telegram utilizzando l'API ufficiale, monitora i canali specificati e reagisce solo quando trova le parole chiave definite dall'utente. Questo permette di rimanere aggiornati su argomenti specifici senza dover scorrere continuamente tutti i messaggi.

Il bot è progettato per uso personale e rispetta la privacy degli utenti, in quanto monitora solo canali pubblici e non memorizza i contenuti dei messaggi. Funziona in background e richiede configurazioni minime per essere operativo.

## Autori
Il progetto è stato sviluppato da:

- **Simon Carbone**

## Tecnologie
Il progetto è stato realizzato con l'aiuto di:

![Python](https://img.icons8.com/color/48/000000/python.png) **Python** - Linguaggio di programmazione utilizzato per lo sviluppo del codice.

![Telegram](https://img.icons8.com/color/e per interagire con la piattaforma Telegram.

![Visual Studio Code](https://img.icons8.com/?size=48&id=9OGIyU8hrxW5&format=png&color=000000) **Visual Studio Code** - Editor di testo e ambiente di sviluppo integrato (IDE) utilizzato per scrivere, eseguire e debuggare il codice.

## Progetto

Per clonare il progetto **FilterBot** e testarlo localmente, segui i seguenti passaggi:

📌 Prerequisiti

- Assicurati di avere Git installato sul tuo sistema.

- Python 3.6 o superiore.

- Le librerie telethon e python-telegram-bot.

🔹 Clonazione del Repository

- Apri il terminale e digita il seguente comando:

  ```bash
   git clone https://github.com/Zimuch/FilterBot-Telegram.git

📦 Installazione delle dipendenze

Installa le librerie necessarie con pip:

    pip install telethon python-telegram-bot

⚙️ Configurazione

Per configurare correttamente il bot dovrei creare/cercare alcune variabili:

- API_ID
- API_HASH
- BOT_TOKEN
- MY_CHAT_ID

Per ottenere API_ID e API_HASH, visita https://my.telegram.org/apps

Per creare un bot e ottenere il BOT_TOKEN, parla con @BotFather su Telegram

Per trovare il tuo MY_CHAT_ID, parla con @userinfobot su Telegram

Modifica il file FilterBot.py per personalizzare i canali da monitorare e le parole chiave:


# Canali da monitorare (username, senza @)
channels = [
    'canale1', 'canale2', 'canale3'
]

# Parole chiave da cercare
keyword = ['parola1', 'parola2', 'parola3']

▶️ Esecuzione

Avvia il bot con il seguente comando:

       python bot.py
       
## Contributors
Al progetto hanno partecipato:

<a href="https://github.com/Zimuch/FilterBot-Telegram/graphs/contributors">
<img src="https://contrib.rocks/image?repo=Zimuch/FilterBot-Telegram" />

</a>
