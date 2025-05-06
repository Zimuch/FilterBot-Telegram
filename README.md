# FilterBot
![English](https://img.icons8.com/color/48/great-britain-circular.png) 

## Introduction
**FilterBot** is a bot designed to monitor messages in public Telegram channels searching for specific keywords. When a match is detected, the bot sends a notification to the user with a direct link to the original message.

The project was born from the need to not miss offers, announcements, or relevant discussions within high-volume channels. Instead of manually checking multiple channels, this bot automates the process by filtering only the content that matches your specific interests.

The approach is simple but effective: the bot connects to Telegram using the official API, monitors the specified channels, and reacts only when it finds the user-defined keywords. This allows you to stay updated on specific topics without having to scroll through all messages continuously.

The bot is designed for personal use and respects user privacy, as it monitors only public channels and does not store message contents. It runs in the background and requires minimal configuration to operate.

## Autors
The project was developed by:

- **Simon Carbone**

## Technologies
The project was built with the help of:

![Python](https://img.icons8.com/color/48/000000/python.png) **Python** - Programming language used for code development.

![Telegram](https://img.icons8.com/color/48/telegram-app--v5.png) **Telegram** - Messaging app used for communication with the bot.

![Visual Studio Code](https://img.icons8.com/?size=48&id=9OGIyU8hrxW5&format=png&color=000000) **Visual Studio Code** - Text editor and integrated development environment (IDE) used to write, run, and debug the code.


## Project

To clone the **FilterBot** project and test it locally, follow these steps: 

📌 Prerequisites

- Make sure Git is installed on your system.

- Python 3.13 or higher.

- The libraries telethon and python-telegram-bot.

🔹  Cloning the Repository

- Open the terminal and type the following command:

  ```bash
   git clone https://github.com/Zimuch/FilterBot-Telegram.git

📦 Installing dependencies

Install the required libraries with pip:

    pip install telethon python-telegram-bot

⚙️ Configuration

To properly configure the bot you need to create/find some variables:

- API_ID
- API_HASH
- BOT_TOKEN
- MY_CHAT_ID

**1) Obtaining API_ID and API_HASH**

To get API_ID and API_HASH from Telegram, follow these steps:

  Visit the site https://my.telegram.org/apps

  Enter your phone number in international format (e.g. +39xxxxxxxxxx for Italy)

  You will receive a confirmation code via the Telegram app (not SMS)

  After entering the code, you will be redirected to a page where you can create a new application

  Fill out the form with the following information:

  App title: a name of your choice for the application (e.g. "FiltroMessaggiBot")

  Short name: a short name without spaces (e.g. "FiltroMessaggiBot")

  Platform: select "Desktop"

  Description: a short description of your bot

  Click on "Create Application"

  On the next page, you will find both the API_ID (a number) and the API_HASH (an alphanumeric string)

  Copy these values and keep them safe; you will need them to configure the bot

  - It is important to note that these credentials are personal and should not be shared publicly.

**2) Creating a bot and obtaining the BOT_TOKEN**

To create a Telegram bot and get its token:

  Open the Telegram app and search for "@BotFather" (make sure it is the official account with the blue checkmark)

  Start a chat with BotFather and send the command /start

  Send the command /newbot to create a new bot

  BotFather will ask you to choose a name for your bot (it can contain spaces)

  Then you must choose a username for the bot that must end with "bot" (e.g. "filtromessaggibot")

  If the name is available, BotFather will provide you with an access token (BOT_TOKEN)

  The token will look like this: 123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ

  Copy this token and keep it safe

  - The BOT_TOKEN is essentially your bot's "password" and allows your script to send messages as the bot. Never share it publicly.
    
**3)  Finding your MY_CHAT_ID**

To find your personal Telegram chat ID:

  Open the Telegram app and search for "@userinfobot" (a bot that provides user information)

  Start a chat with userinfobot and send the command /start

  The bot will immediately reply with your information, including your ID

  The message will look like this:


Id: 12345678
First: [name]
Last: [surname]
Username: [username]

  The number after "Id:" is your MY_CHAT_ID

  Copy this number and use it in the bot configuration

  This ID is necessary so the bot knows whom to send notifications to when it finds matches with keywords.

Modify the file FilterBot.py to customize the channels to monitor and the keywords:
  - To add a channel, simply add the public channel username (without '@') inside the channels variable
  - To add a keyword, simply add your search word inside the keyword variable

## Channels to monitor (username, without @)
channels = [
    'canale1', 'canale2', 'canale3'
]

## Keywords to search for
keyword = ['parola1', 'parola2', 'parola3']

▶️ Running the bot

Start the bot with the following command:

       python bot.py


## Contributors
the project was attended by:

<a href="https://github.com/Zimuch/FilterBot-Telegram/graphs/contributors">
<img src="https://contrib.rocks/image?repo=Zimuch/FilterBot-Telegram" />

</a>

## Disclaimer
This project is provided for informational and academic purposes only.
The author assumes no responsibility for any misuse or damages arising from the use of this software.
Users are solely responsible for complying with all applicable laws and Telegram's terms of service when using this bot.
By using this project, you agree that the author is not liable for any consequences resulting from its deployment or operation.

# FilterBot
![Italiano](https://img.icons8.com/color/48/italy-circular.png) 

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

![Telegram](https://img.icons8.com/color/48/telegram-app--v5.png) **Telegram** - App di messaggistica utilizzata per la comunicazione con il bot.

![Visual Studio Code](https://img.icons8.com/?size=48&id=9OGIyU8hrxW5&format=png&color=000000) **Visual Studio Code** - Editor di testo e ambiente di sviluppo integrato (IDE) utilizzato per scrivere, eseguire e debuggare il codice.

## Progetto

Per clonare il progetto **FilterBot** e testarlo localmente, segui i seguenti passaggi:

📌 Prerequisiti

- Assicurati di avere Git installato sul tuo sistema.

- Python 3.13 o superiore.

- Le librerie telethon e python-telegram-bot.

🔹 Clonazione del Repository

- Apri il terminale e digita il seguente comando:

  ```bash
   git clone https://github.com/Zimuch/FilterBot-Telegram.git

📦 Installazione delle dipendenze

Installa le librerie necessarie con pip:

    pip install telethon python-telegram-bot

⚙️ Configurazione

Per configurare correttamente il bot dovrai creare/cercare alcune variabili:

- API_ID
- API_HASH
- BOT_TOKEN
- MY_CHAT_ID

**1) Ottenere API_ID e API_HASH**

Per ottenere API_ID e API_HASH da Telegram, devi seguire questi passaggi:

Visita il sito https://my.telegram.org/apps

Inserisci il tuo numero di telefono in formato internazionale (es. +39xxxxxxxxxx per l'Italia)

Riceverai un codice di conferma tramite l'app Telegram (non via SMS)

Dopo aver inserito il codice, verrai reindirizzato a una pagina dove potrai creare una nuova applicazione

Compila il modulo con le seguenti informazioni:

App title: un nome a tua scelta per l'applicazione (es. "FiltroMessaggiBot")

Short name: un nome breve senza spazi (es. "FiltroMessaggiBot")

Platform: seleziona "Desktop"

Description: una breve descrizione del tuo bot

Clicca su "Create Application"

Nella pagina successiva, troverai sia l'API_ID (un numero) che l'API_HASH (una stringa alfanumerica)

Copia questi valori e conservali in modo sicuro, ti serviranno per configurare il bot

- È importante notare che queste credenziali sono personali e non dovrebbero essere condivise pubblicamente.

**2) Creare un bot e ottenere il BOT_TOKEN**

Per creare un bot Telegram e ottenere il relativo token:

Apri l'app Telegram e cerca "@BotFather" (verifica che sia l'account ufficiale con il segno di spunta blu)

Avvia una chat con BotFather e invia il comando /start

Invia il comando /newbot per creare un nuovo bot

BotFather ti chiederà di scegliere un nome per il tuo bot (può contenere spazi)

Successivamente, dovrai scegliere un username per il bot che deve terminare con "bot" (es. "filtromessaggibot")

Se il nome è disponibile, BotFather ti fornirà un token di accesso (BOT_TOKEN)

Il token sarà simile a questo: 123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ

Copia questo token e conservalo in modo sicuro

- Il BOT_TOKEN è essenzialmente la "password" del tuo bot e consente al tuo script di inviare messaggi come se fosse il bot. Non condividerlo mai pubblicamente.

**3) Trovare il tuo MY_CHAT_ID**

Per trovare il tuo ID chat personale su Telegram:

Apri l'app Telegram e cerca "@userinfobot" (un bot che fornisce informazioni sull'utente)

Avvia una chat con userinfobot e invia il comando /start

Il bot risponderà immediatamente con le tue informazioni, incluso il tuo ID

Il messaggio sarà simile a questo:


Id: 12345678
First: [Il tuo nome]
Last: [Il tuo cognome]
Username: [Il tuo username]

Il numero dopo "Id:" è il tuo MY_CHAT_ID

Copia questo numero e usalo nella configurazione del bot

- Questo ID è necessario affinché il bot sappia a chi inviare le notifiche quando trova corrispondenze con le parole chiave.

- Modifica il file FilterBot.py per personalizzare i canali da monitorare e le parole chiave:
   - Per inserire un canale ti basta aggiungere all'interno della variabile **channels** il canale pubblico (tra '')
   - Per inserire una keyword ti basta aggiungere all'interno della variabile **keyword** la tua parola da ricercare (tra '')

## Canali da monitorare (username, senza @)
channels = [
    'canale1', 'canale2', 'canale3'
]

## Parole chiave da cercare
keyword = ['parola1', 'parola2', 'parola3']

▶️ Esecuzione

Avvia il bot con il seguente comando:

       python bot.py


       
## Contributors
Al progetto hanno partecipato:

<a href="https://github.com/Zimuch/FilterBot-Telegram/graphs/contributors">
<img src="https://contrib.rocks/image?repo=Zimuch/FilterBot-Telegram" />

</a>

## Disclaimer
Questo progetto è fornito a solo scopo informativo e accademico.
L'autore non si assume alcuna responsabilità per eventuali usi impropri o danni derivanti dall'utilizzo di questo software.
Gli utenti sono gli unici responsabili del rispetto di tutte le leggi applicabili e dei termini di servizio di Telegram durante l'uso di questo bot.
Utilizzando questo progetto, l'utente accetta che l'autore non è responsabile per eventuali conseguenze derivanti dal suo utilizzo o funzionamento.
