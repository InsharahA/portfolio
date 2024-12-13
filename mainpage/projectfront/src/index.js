import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

document.addEventListener('DOMContentLoaded', () => {
  const container = document.getElementById('app-container'); // Target the container
  if (container) {
    const root = ReactDOM.createRoot(container); // Create root
    root.render(<App />); // Render the React App
  } else {
    console.error('Target container not found: #app-container');
  }
});

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
