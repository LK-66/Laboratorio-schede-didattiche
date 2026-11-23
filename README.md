# Schede didattiche

Sito con le dashboard di studio per gli allievi, preparate con il **Laboratorio Schede**.

**Link per gli allievi:** https://lk-66.github.io/Laboratorio-schede-didattiche/

Ogni scheda ha lettura guidata con voce, disegni interattivi, infografica, glossario, flashcard, quiz e, se presenti, mappe mentali e quiz interattivi. Funziona su computer, iPad e telefono (in Safari: Condividi › Aggiungi alla schermata Home).

## Come aggiungere o aggiornare una scheda

1. Nel Laboratorio Schede V3 (su claude.ai) apri la dashboard e premi **⬇ Esporta**.
2. Manda il file HTML a Claude in chat: Claude lo carica qui con `strumenti/aggiungi_dash.py`.
3. Dopo 1–2 minuti la scheda è online. Se aggiorni una scheda già pubblicata (stesso titolo e materia), il link resta lo stesso.

## Struttura

- `index.html` – pagina iniziale con le schede divise per materia (legge `dashboards.json`)
- `<materia>/<titolo>.html` – una dashboard per file, funziona anche da sola (es. su Moodle)
- `laboratorio/laboratorio-v3.html` – **copia di riserva** del codice del Laboratorio V3. Funziona solo dentro claude.ai (usa Claude e l'archivio di claude.ai): qui serve come backup e cronologia delle versioni.
- `strumenti/aggiungi_dash.py` – aggiunge una dashboard esportata al sito
