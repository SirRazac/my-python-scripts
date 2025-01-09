# ------------------------------------------------------------------------------
# Initialize Firebase
# ------------------------------------------------------------------------------
import firebase_admin
from firebase_admin import credentials, messaging
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

# Path to the 'firebase-adminsdk-xxxx.json' file
cred = credentials.Certificate("firebaseKey.json")
firebase_admin.initialize_app(cred)

# Firebase device token (e.g., from a web app, test device, etc.)
device_token = os.getenv('FIREBASE_DEVICE_TOKEN')
print("Device Token:", device_token)  # Gib den Token aus, um sicherzustellen, dass er korrekt geladen wurde

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
