self.addEventListener('install', (event) => {
  console.log('Service Worker installiert');
});

self.addEventListener('activate', (event) => {
  console.log('Service Worker aktiviert');
});

// Empfangen von Push-Nachrichten im Hintergrund
self.addEventListener('push', (event) => {
  const payload = event.data.json();
  console.log("Push-Nachricht empfangen: ", payload);

  const notificationTitle = payload.title || 'Neue Nachricht';
  const notificationOptions = {
    body: payload.body || 'Du hast eine neue Nachricht.',
  };

  event.waitUntil(
    self.registration.showNotification(notificationTitle, notificationOptions)
  );
});
