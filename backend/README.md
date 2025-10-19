# Flask Backend

Ein einfaches Flask Backend mit REST API.

## Installation

```bash
# Virtuelle Umgebung erstellen
python -m venv venv

# Virtuelle Umgebung aktivieren
# Auf macOS/Linux:
source venv/bin/activate
# Auf Windows:
# venv\Scripts\activate

# Dependencies installieren
pip install -r requirements.txt
```

## Starten

```bash
python app.py
```

Der Server läuft dann auf `http://localhost:5000`

## API Endpoints

- `GET /` - Status check
- `GET /api/hello?name=YourName` - Greeting endpoint
- `POST /api/data` - Send JSON data
