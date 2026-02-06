import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

const resources = {
  en: {
    translation: {
      appTitle: 'Financial Health Assessment Tool',
      // Add more keys as needed
    },
  },
  hi: {
    translation: {
      appTitle: 'वित्तीय स्वास्थ्य मूल्यांकन उपकरण',
      // Add Hindi translations
    },
  },
};

i18n.use(initReactI18next).init({
  resources,
  lng: 'en',  // Default language
  fallbackLng: 'en',
  interpolation: { escapeValue: false },
});

export default i18n;