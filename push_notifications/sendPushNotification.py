import firebase_admin
from firebase_admin import credentials, messaging

# Pfad zur 'firebase-adminsdk-xxxx.json' Datei
cred = credentials.Certificate("firebaseKey.json")
firebase_admin.initialize_app(cred)

# Dein Firebase-Gerätetoken (z.B. von einer Web-App, einem Testgerät, etc.)
device_token = "dFhaY8RzRHxwc4suWsmUEO:APA91bH6rGX81Gm5IyLkvJNanK8ab8lwe3AfwtrgIXFDB5VJkqW34RnPSSoZhowZN-iZxHzCZSPw6xjlAc9St5MY8abiLXptrGzntIcvBoxuBlHbovQA-h4"

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
