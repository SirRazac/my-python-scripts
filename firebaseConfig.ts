<script type="module">
  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/11.1.0/firebase-app.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/11.1.0/firebase-analytics.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
    apiKey: "AIzaSyBwVoTWR6lqBK8BUsQK12l_UQfWLvs_eNo",
    authDomain: "pushtest-a8d7a.firebaseapp.com",
    projectId: "pushtest-a8d7a",
    storageBucket: "pushtest-a8d7a.firebasestorage.app",
    messagingSenderId: "464581164056",
    appId: "1:464581164056:web:5ed0e5c4b7735ff4fc976d",
    measurementId: "G-G20G63ZYCF"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);
</script>