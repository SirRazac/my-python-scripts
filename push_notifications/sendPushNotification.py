import firebase_admin
from firebase_admin import credentials, messaging

# Pfad zur 'firebase-adminsdk-xxxx.json' Datei
cred = credentials.Certificate("firebaseKey.json")
firebase_admin.initialize_app(cred)

# Dein Firebase-Gerätetoken (z.B. von einer Web-App, einem Testgerät, etc.)
device_token = "c-0uG7pjH8gcpg6lvQMLkf:APA91bF3F_hkoCbqnSBzOAsahmEy0oJTAJKtxyIoBDcSQgrMvaQjfSfSUH2v8A21_Z1_YL8OXMiNQAOmm7UFVA-PhMN-ODireL45-Ep4V2gQ0nGPXBJYEBM"

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
