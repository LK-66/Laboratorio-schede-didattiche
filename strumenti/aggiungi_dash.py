"""Aggiunge (o aggiorna) una dashboard esportata dal Laboratorio Schede al sito.

Uso:  python3 strumenti/aggiungi_dash.py percorso/dashboard.html
La dashboard finisce in <materia>/<titolo>.html e compare nella pagina iniziale.
Se esiste già una dashboard con lo stesso titolo e materia, viene sostituita (il link resta uguale).
"""
import json, re, sys, unicodedata, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
MARK = "DashRender.mount(document.getElementById('app'), "

def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')[:60] or 'scheda'

def main(path):
    html = pathlib.Path(path).read_text(encoding='utf8')
    i = html.find(MARK)
    if i < 0: sys.exit('Non sembra una dashboard esportata dal Laboratorio.')
    data, _ = json.JSONDecoder().raw_decode(html, i + len(MARK))
    subject = (data.get('subject') or 'Altro').strip() or 'Altro'
    folder, name = slug(subject), slug(data.get('title') or 'scheda') + '.html'
    # link per tornare alla pagina iniziale + icona per la schermata Home
    home = ('<a href="../" style="display:inline-block;margin:10px 12px 0;font:700 15px Nunito,system-ui,sans-serif;'
            'color:#2457A6;text-decoration:none">← Tutte le schede</a>')
    html = re.sub(r'<body>', '<body>' + home, html, count=1)
    html = html.replace('</head>', '<link rel="apple-touch-icon" href="../icon.png"><link rel="icon" href="../icon.png"></head>', 1)
    (ROOT / folder).mkdir(exist_ok=True)
    (ROOT / folder / name).write_text(html, encoding='utf8')
    lst_path = ROOT / 'dashboards.json'
    lst = json.loads(lst_path.read_text(encoding='utf8')) if lst_path.exists() else []
    lst = [d for d in lst if d['file'] != f'{folder}/{name}']
    lst.append({
        'file': f'{folder}/{name}', 'title': data.get('title', ''), 'subject': subject, 'level': data.get('level', ''),
        'emoji': data.get('emoji', ''), 'intro': re.sub(r'\*\*', '', data.get('intro', ''))[:220],
        'extra': {k: len(data.get(k) or []) for k in ('diagrams', 'maps', 'quizzes')},
        'updated': datetime.date.today().isoformat()})
    lst.sort(key=lambda d: (d['subject'].lower(), d['title'].lower()))
    lst_path.write_text(json.dumps(lst, ensure_ascii=False, indent=1), encoding='utf8')
    print('OK:', f'{folder}/{name}')

if __name__ == '__main__':
    for p in sys.argv[1:] or sys.exit(__doc__): main(p)
