import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';  // Keep default
import App from './App';
import './i18n';  // Add this line to initialize translations

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);