#!/usr/bin/env python3
"""
Markdown Visualizer - Un'applicazione per visualizzare file Markdown
"""

import os
from pathlib import Path
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, jsonify, send_from_directory
import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.tables import TableExtension
from markdown.extensions.toc import TocExtension

app = Flask(__name__)

# Directory di default per i file markdown
DEFAULT_MD_DIR = os.path.dirname(os.path.abspath(__file__))

# Configurazione upload
UPLOAD_FOLDER = os.path.join(DEFAULT_MD_DIR, 'uploads')
ALLOWED_EXTENSIONS = {'md', 'markdown', 'txt'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Max 16MB

# Crea la cartella uploads se non esiste
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename: str) -> bool:
    """Verifica se l'estensione del file è permessa."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_markdown_files(directory: str = None) -> list:
    """Restituisce la lista dei file markdown nella directory specificata."""
    if directory is None:
        directory = DEFAULT_MD_DIR
    
    md_files = []
    path = Path(directory)
    
    if path.exists():
        for file in sorted(path.glob("**/*.md")):
            relative_path = file.relative_to(path)
            md_files.append({
                "name": file.name,
                "path": str(file),
                "relative_path": str(relative_path),
                "size": file.stat().st_size,
                "modified": file.stat().st_mtime
            })
    
    return md_files


def render_markdown(filepath: str) -> dict:
    """Converte un file markdown in HTML."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        md = markdown.Markdown(extensions=[
            'fenced_code',
            'tables',
            'toc',
            'nl2br',
            'sane_lists',
            CodeHiliteExtension(css_class='highlight', linenums=False),
            TocExtension(title='Indice', toc_depth=3)
        ])
        
        html_content = md.convert(content)
        toc = md.toc
        
        return {
            "success": True,
            "html": html_content,
            "toc": toc,
            "raw": content
        }
    except FileNotFoundError:
        return {"success": False, "error": "File non trovato"}
    except Exception as e:
        return {"success": False, "error": str(e)}


@app.route('/')
def index():
    """Pagina principale."""
    files = get_markdown_files()
    return render_template('index.html', files=files)


@app.route('/api/files')
def api_files():
    """API per ottenere la lista dei file."""
    directory = request.args.get('dir', DEFAULT_MD_DIR)
    files = get_markdown_files(directory)
    return jsonify(files)


@app.route('/api/render')
def api_render():
    """API per renderizzare un file markdown."""
    filepath = request.args.get('file')
    if not filepath:
        return jsonify({"success": False, "error": "Nessun file specificato"})
    
    # Sicurezza: verifica che il file esista e sia un .md
    if not filepath.endswith('.md'):
        return jsonify({"success": False, "error": "Solo file .md sono permessi"})
    
    return jsonify(render_markdown(filepath))


@app.route('/api/preview', methods=['POST'])
def api_preview():
    """API per preview di markdown raw."""
    data = request.get_json()
    content = data.get('content', '')
    
    md = markdown.Markdown(extensions=[
        'fenced_code',
        'tables',
        'toc',
        'nl2br',
        'sane_lists',
        CodeHiliteExtension(css_class='highlight', linenums=False)
    ])
    
    html_content = md.convert(content)
    
    return jsonify({"success": True, "html": html_content})


@app.route('/api/upload', methods=['POST'])
def api_upload():
    """API per caricare un file markdown."""
    if 'file' not in request.files:
        return jsonify({"success": False, "error": "Nessun file selezionato"})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"success": False, "error": "Nessun file selezionato"})
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        
        # Se non ha estensione .md, aggiungila
        if not filename.endswith('.md'):
            filename = filename.rsplit('.', 1)[0] + '.md'
        
        # Gestisci nomi duplicati
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        base_name = filename.rsplit('.', 1)[0]
        counter = 1
        while os.path.exists(filepath):
            filename = f"{base_name}_{counter}.md"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            counter += 1
        
        file.save(filepath)
        
        return jsonify({
            "success": True,
            "filename": filename,
            "path": filepath,
            "message": f"File '{filename}' caricato con successo"
        })
    
    return jsonify({
        "success": False,
        "error": "Tipo di file non permesso. Usa .md, .markdown o .txt"
    })


@app.route('/api/upload-content', methods=['POST'])
def api_upload_content():
    """API per visualizzare direttamente contenuto markdown senza salvare."""
    data = request.get_json()
    content = data.get('content', '')
    filename = data.get('filename', 'Contenuto caricato')
    
    md = markdown.Markdown(extensions=[
        'fenced_code',
        'tables',
        'toc',
        'nl2br',
        'sane_lists',
        CodeHiliteExtension(css_class='highlight', linenums=False),
        TocExtension(title='Indice', toc_depth=3)
    ])
    
    html_content = md.convert(content)
    toc = md.toc
    
    return jsonify({
        "success": True,
        "html": html_content,
        "toc": toc,
        "raw": content,
        "filename": filename
    })


if __name__ == '__main__':
    print("\n" + "="*50)
    print("  Markdown Visualizer")
    print("  Apri http://localhost:5000 nel browser")
    print("="*50 + "\n")
    app.run(debug=True, host='0.0.0.0', port=5000)
