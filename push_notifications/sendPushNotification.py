import firebase_admin
from firebase_admin import credentials, messaging

# Path to the 'firebase-adminsdk-xxxx.json' file
cred = credentials.Certificate("firebaseKey.json")
firebase_admin.initialize_app(cred)

# Firebase device token (e.g., from a web app, test device, etc.)
device_token = "c-0uG7pjH8gcpg6lvQMLkf:APA91bF3F_hkoCbqnSBzOAsahmEy0oJTAJKtxyIoBDcSQgrMvaQjfSfSUH2v8A21_Z1_YL8OXMiNQAOmm7UFVA-PhMN-ODireL45-Ep4V2gQ0nGPXBJYEBM"

# Create a message
message = messaging.Message(
    notification=messaging.Notification(
        title="Test Push Nachricht",
        body="Dies ist eine Testnachricht!"
    ),
    token=device_token,
)

# Send the message
response = messaging.send(message)
print('Nachricht gesendet: ', response)
