# Markdown Visualizer

Un'applicazione Python con interfaccia web moderna per visualizzare e modificare file Markdown.

## Caratteristiche

### Visualizzazione
- 📖 **Rendering Markdown completo** - Supporto per tabelle, codice, liste, link e molto altro
- 🎨 **Syntax Highlighting** - Colorazione del codice per numerosi linguaggi
- 🌙 **Tema Chiaro/Scuro** - Cambia tema con un click
- 📑 **Indice automatico** - Generazione automatica dell'indice (TOC)
- 👁️ **Modalità multiple** - Preview, Raw (sorgente) e Split view

### Editor
- ✏️ **Editor integrato** - Modifica i file direttamente nell'applicazione
- ⚡ **Preview live** - Visualizza le modifiche in tempo reale mentre scrivi
- 💾 **Salvataggio** - Salva le modifiche con un click o scorciatoia
- 🔄 **Toggle Visualizza/Modifica** - Passa facilmente tra lettura e modifica

### Gestione File
- 📤 **Upload file** - Carica file .md, .markdown o .txt
- 🎯 **Drag & Drop** - Trascina i file direttamente nell'applicazione
- 🔍 **Ricerca file** - Cerca rapidamente tra i file .md
- 📁 **Salvataggio opzionale** - Scegli se salvare sul server o solo visualizzare

## Installazione

1. **Clona o scarica** il progetto

2. **Crea un ambiente virtuale** (consigliato):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # oppure
   venv\Scripts\activate  # Windows
   ```

3. **Installa le dipendenze**:
   ```bash
   pip install -r requirements.txt
   ```

## Utilizzo

1. **Avvia l'applicazione**:
   ```bash
   python app.py
   ```

2. **Apri il browser** all'indirizzo:
   ```
   http://localhost:5000
   ```

3. **Seleziona un file** dalla barra laterale per visualizzarlo

4. **Per modificare**: clicca su "✏️ Modifica" o premi `Ctrl+E`

5. **Per salvare**: clicca su "💾 Salva" o premi `Ctrl+S`

## Scorciatoie da Tastiera

| Scorciatoia | Azione |
|-------------|--------|
| `Ctrl + O` | Apri/Carica file |
| `Ctrl + E` | Toggle Modifica/Visualizza |
| `Ctrl + S` | Salva file |
| `Ctrl + T` | Cambia tema chiaro/scuro |

## Modalità di Visualizzazione

- **Preview**: Rendering completo del Markdown con stili
- **Raw (Sorgente)**: Visualizza il codice sorgente del file
  - Modalità lettura: visualizzazione pulita read-only
  - Modalità modifica: editor con preview live
- **Split**: Vista divisa con sorgente a sinistra e preview a destra

## Struttura del Progetto

```
markdown-visualizer/
├── app.py              # Applicazione Flask principale
├── requirements.txt    # Dipendenze Python
├── README.md           # Questo file
├── uploads/            # Cartella per i file caricati
├── templates/
│   └── index.html      # Template HTML principale
└── static/
    └── style.css       # Stili CSS
```

## Tecnologie Utilizzate

- **Backend**: Flask
- **Markdown Parser**: python-markdown
- **Syntax Highlighting**: Pygments + Highlight.js
- **Frontend**: HTML5, CSS3, JavaScript vanilla

## Personalizzazione

### Cambiare la directory dei file

Modifica la variabile `DEFAULT_MD_DIR` in `app.py` per specificare una directory diversa:

```python
DEFAULT_MD_DIR = "/percorso/alla/tua/cartella"
```

### Cambiare la porta

Modifica la chiamata a `app.run()` in `app.py`:

```python
app.run(debug=True, host='0.0.0.0', port=8080)
```

## API Endpoints

| Endpoint | Metodo | Descrizione |
|----------|--------|-------------|
| `/` | GET | Pagina principale |
| `/api/files` | GET | Lista dei file markdown |
| `/api/render` | GET | Renderizza un file markdown |
| `/api/preview` | POST | Preview di contenuto markdown |
| `/api/upload` | POST | Carica un file |
| `/api/save` | POST | Salva modifiche a un file |

## Licenza

MIT License - Sentiti libero di usare e modificare questo progetto.
