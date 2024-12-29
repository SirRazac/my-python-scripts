# My Python Scripts

Dies ist ein Repository, das verschiedene kleine Python-Skripte enthält, die ich geschrieben habe, um verschiedene Konzepte und Techniken zu lernen. Ein besonderes Feature dieses Repositories ist die Integration von Push-Benachrichtigungen, die mithilfe von **Firebase** und einem lokalen Server, der mit **Ngrok** öffentlich zugänglich gemacht wird, realisiert wird.

## Verzeichnisstruktur

- `data_structures/`: Skripte zu verschiedenen Datenstrukturen wie Linked Lists, Stacks, Queues usw.
  - Beispiel: `data_structures/linked_list.py`: Eine einfache Implementierung einer verketteten Liste.
- `algorithms/`: Implementierungen von Algorithmen wie Sortieralgorithmen und Suchalgorithmen.
  - Beispiel: `algorithms/sorting.py`: Implementierung des Bubble Sort Algorithmus.
- `web_scraping/`: Skripte zum Extrahieren von Informationen aus Webseiten.
  - Beispiel: `web_scraping/weather_scraper.py`: Scraping von Wetterdaten von einer Beispielseite (bitte URL anpassen).
- `automation/`: Automatisierungs-Skripte für alltägliche Aufgaben.
  - Beispiel: `automation/file_rename.py`: Umbenennen von Dateien in einem Verzeichnis.
- `push_notifications/`: Skripte zur Implementierung von Push-Benachrichtigungen mit Firebase und Ngrok.
  - Beispiel: `push_notifications/send_notification.py`: Beispiel für das Senden einer Push-Benachrichtigung an ein Gerät über Firebase.

## Firebase und Ngrok für Push-Benachrichtigungen

In diesem Repository wird **Firebase Cloud Messaging (FCM)** verwendet, um Push-Benachrichtigungen an Geräte zu senden. Um das lokale Backend mit einer HTTPS-URL öffentlich zugänglich zu machen, wird **Ngrok** eingesetzt. Dies ist notwendig, damit Firebase sicher mit dem lokalen Server kommunizieren und Benachrichtigungen verschicken kann.

### Firebase Cloud Messaging
- **Firebase Cloud Messaging (FCM)** wird verwendet, um Push-Benachrichtigungen an Geräte zu senden.
- Um FCM zu nutzen, musst du ein Firebase-Projekt erstellen und die entsprechenden API-Schlüssel sowie die Geräte-Token erhalten, an die du Nachrichten senden möchtest.

### Ngrok für lokale Entwicklung
- **Ngrok** wird verwendet, um deinen lokalen Entwicklungsserver sicher über eine HTTPS-URL öffentlich zugänglich zu machen.
- Ngrok tunnelt den Verkehr von einer öffentlichen URL zu deinem lokalen Server, sodass du Firebase Cloud Messaging auch während der Entwicklung mit einem lokalen Backend nutzen kannst.
- **Ngrok wird außerdem genutzt, um das Gerätetoken des mobilen Endgeräts zu erhalten.** Indem der lokale Server mit einer öffentlich zugänglichen URL über Ngrok erreichbar ist, kann das mobile Endgerät mit Firebase kommunizieren, und du kannst das benötigte Token abrufen, um später Push-Benachrichtigungen zu senden.
- Um Ngrok zu verwenden, musst du es installieren und dann den Befehl `ngrok http 3000` ausführen, um eine öffentlich zugängliche HTTPS-URL zu erhalten.

## Installation

1. **Firebase Setup**
   - Erstelle ein Firebase-Projekt und aktiviere Firebase Cloud Messaging.
   - Erhalte die **Server-Sicherheitsschlüssel** und die **Geräte-Token** für Push-Benachrichtigungen.

2. **Ngrok Setup**
   - Installiere [Ngrok](https://ngrok.com/) und stelle sicher, dass es korrekt eingerichtet ist.
   - Starte den Tunnel mit folgendem Befehl:
     ```bash
     ngrok http 3000
     ```
   - Du erhältst eine öffentliche HTTPS-URL, die du für Firebase verwenden kannst.

3. **Python Abhängigkeiten**
   - Stelle sicher, dass du alle nötigen Python-Abhängigkeiten installiert hast. Falls noch nicht geschehen, führe folgendes aus:
     ```bash
     pip install -r requirements.txt
     ```

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert.
