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

![Telegram](https://img.icons8.com/color/48/telegram-app--v5.png) per interagire con la piattaforma Telegram.

![Visual Studio Code](https://img.icons8.com/?size=48&id=9OGIyU8hrxW5&format=png&color=000000) **Visual Studio Code** - Editor di testo e ambiente di sviluppo integrato (IDE) utilizzato per scrivere, eseguire e debuggare il codice.

## Progetto

Per clonare il progetto **FilterBot** e testarlo localmente, segui i seguenti passaggi:

📌 Prerequisiti

- Assicurati di avere Git installato sul tuo sistema.

- Python 3.6 o superiore.

- Le librerie telethon e python-telegram-bot==13.5.

🔹 Clonazione del Repository

- Apri il terminale e digita il seguente comando:

  ```bash
   git clone https://github.com/Zimuch/FilterBot-Telegram.git

📦 Installazione delle dipendenze

Installa le librerie necessarie con pip:

    pip install telethon python-telegram-bot==13.5

⚙️ Configurazione

Per configurare correttamente il bot dovrei creare/cercare alcune variabili:

- API_ID
- API_HASH
- BOT_TOKEN
- MY_CHAT_ID

**Ottenere API_ID e API_HASH**

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

- È importante notare che queste credenziali sono personali e non dovrebbero essere condivise pubblicamente o incluse direttamente nel codice che carichi su GitHub.

**Creare un bot e ottenere il BOT_TOKEN**

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

**Trovare il tuo MY_CHAT_ID**

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

- Questo ID è necessario affinché il bot sappia a chi inviare le notifiche quando trova corrispondenze con le parole chiave. Nel tuo codice, hai impostato che le notifiche vengano inviate solo al tuo account personale.

- Modifica il file FilterBot.py per personalizzare i canali da monitorare e le parole chiave:


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
