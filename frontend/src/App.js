import React, { useState } from 'react';
import './App.css';  // Keep this for styling
import Upload from './components/Upload';  // Import Upload component
import Dashboard from './components/Dashboard';  // Import Dashboard component
import { useTranslation } from 'react-i18next';  // For multilingual support
import { FaLanguage } from 'react-icons/fa';  // Icon for language buttons

function App() {
  const { t, i18n } = useTranslation();  // Hook for translations
  const [insights, setInsights] = useState('');  // State for AI insights
  const [financialData, setFinancialData] = useState({});  // State for chart data

  // Function to handle data from Upload component
  const handleInsights = (data) => {
    setInsights(data.insights);
    setFinancialData(data.financialData || {});
  };

  // Function to change language
  const changeLanguage = (lng) => {
    i18n.changeLanguage(lng);
  };

  return (
    <div className="App">
      {/* Attractive header with title and language switcher */}
      <header className="App-header">
        <h1>{t('appTitle')}</h1>  {/* Translated title */}
        <button onClick={() => changeLanguage('en')}><FaLanguage /> English</button>
        <button onClick={() => changeLanguage('hi')}><FaLanguage /> Hindi</button>
      </header>

      {/* Main content area */}
      <main>
        <Upload onInsights={handleInsights} />  {/* Pass callback for data */}
        <Dashboard insights={insights} data={financialData} />  {/* Pass data for visualization */}
      </main>
    </div>
  );
}

export default App;