import firebase_admin
from firebase_admin import credentials, messaging

# Pfad zur 'firebase-adminsdk-xxxx.json' Datei
cred = credentials.Certificate("path/to/your/firebase-adminsdk-xxxx.json")
firebase_admin.initialize_app(cred)

# Dein Firebase-Gerätetoken (z.B. von einer Web-App, einem Testgerät, etc.)
device_token = "DEIN_EIGENER_FCM_TOKEN"

# Erstelle eine Nachricht
message = messaging.Message(
    notification=messaging.Notification(
        title="Test Push Nachricht",
        body="Dies ist eine Testnachricht!"
    ),
    token=device_token,
)

# Sende die Nachricht
response = messaging.send(message)
print('Nachricht gesendet: ', response)
