# Telegram Bot

Ein einfacher Telegram Bot, der alle Nachrichten abruft und verarbeitet.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Bot Token einsetzen:
   - Öffne `bot.py`
   - Ersetze `YOUR_BOT_TOKEN_HERE` mit deinem echten Bot Token

3. Bot starten:
```bash
python bot.py
```

## Funktionen

- Ruft kontinuierlich neue Nachrichten ab
- Zeigt empfangene Nachrichten in der Konsole an
- Sendet Echo-Antworten zurück

## Bot Token erhalten

1. Starte einen Chat mit @BotFather auf Telegram
2. Sende `/newbot`
3. Folge den Anweisungen
4. Kopiere den erhaltenen Token in die `bot.py` Datei