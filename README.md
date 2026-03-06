# Markdown Visualizer

Un'applicazione Python con interfaccia web moderna per visualizzare file Markdown.

## Caratteristiche

- 📖 **Rendering Markdown completo** - Supporto per tabelle, codice, liste, link e molto altro
- 🎨 **Syntax Highlighting** - Colorazione del codice per numerosi linguaggi
- 🌙 **Tema Chiaro/Scuro** - Cambia tema con un click
- 📑 **Indice automatico** - Generazione automatica dell'indice (TOC)
- 👁️ **Modalità multiple** - Preview, Raw e Split view
- 🔍 **Ricerca file** - Cerca rapidamente tra i file .md
- ⚡ **Aggiornamento live** - Aggiorna la lista file senza ricaricare

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

## Scorciatoie da Tastiera

| Scorciatoia | Azione |
|-------------|--------|
| `Ctrl + T` | Cambia tema chiaro/scuro |

## Struttura del Progetto

```
markdown-visualizer/
├── app.py              # Applicazione Flask principale
├── requirements.txt    # Dipendenze Python
├── README.md          # Questo file
├── templates/
│   └── index.html     # Template HTML principale
└── static/
    └── style.css      # Stili CSS
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

## Licenza

MIT License - Sentiti libero di usare e modificare questo progetto.
