import firebase_admin
from firebase_admin import credentials, messaging

# Pfad zur 'firebase-adminsdk-xxxx.json' Datei
cred = credentials.Certificate("firebaseKey.json")
firebase_admin.initialize_app(cred)

# Dein Firebase-Gerätetoken (z.B. von einer Web-App, einem Testgerät, etc.)
device_token = "dROYdjQt3kajZEre1se45F:APA91bHOP10wHOuSIYDwXw8kdXZXE0QSKduCQi6gTXaLHcskWyZn0Y9o27zp-IX2bdYUWc0Aeea1J8ertfU33z5WoxZNqeN4u6gbtKjuOn8ciI5iVAG_PXQ"

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
