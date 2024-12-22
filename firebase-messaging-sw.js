// Importiere Firebase und Firebase Messaging
importScripts('https://www.gstatic.com/firebasejs/9.0.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/9.0.0/firebase-messaging.js');

// Firebase-Konfiguration
const firebaseConfig = {
  apiKey: "AIzaSyBwVoTWR6lqBK8BUsQK12l_UQfWLvs_eNo",
  authDomain: "pushtest-a8d7a.firebaseapp.com",
  projectId: "pushtest-a8d7a",
  storageBucket: "pushtest-a8d7a.firebasestorage.app",
  messagingSenderId: "464581164056",
  appId: "1:464581164056:web:5ed0e5c4b7735ff4fc976d",
  measurementId: "G-G20G63ZYCF",
};

// Firebase initialisieren
firebase.initializeApp(firebaseConfig);

// Firebase Messaging initialisieren
const messaging = firebase.messaging();

// Empfang von Hintergrundnachrichten
messaging.onBackgroundMessage(function(payload) {
  console.log('Hintergrund-Nachricht empfangen ', payload);
  const notificationTitle = 'Hintergrundbenachrichtigung';
  const notificationOptions = {
    body: payload.body,
  };

  self.registration.showNotification(notificationTitle, notificationOptions);
});
