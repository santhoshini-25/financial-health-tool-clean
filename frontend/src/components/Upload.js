import React, { useState } from 'react';
import axios from 'axios';

function Upload({ onInsights }) {  // Receive onInsights prop from App.js
  const [file, setFile] = useState(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);  // For loading state

  const handleUpload = async () => {
    if (!file) {
      setError('Please select a file first.');
      return;
    }

    setLoading(true);  // Start loading
    setError('');  // Clear previous errors

    const formData = new FormData();
    formData.append('file', file);
    formData.append('industry', 'Manufacturing');  // Default industry; can make this a dropdown later

    try {
      const API_URL = process.env.REACT_APP_API_URL || 'http://127.0.0.1:8000'; 
      const response = await axios.post(`${API_URL}/upload`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      
      // Pass data to App.js for state management
      onInsights({
        insights: response.data.insights,
        financialData: response.data.data || {}  // Backend returns 'data' with revenue/expenses
      });
    } catch (err) {
      console.error('Upload error:', err);  // Log for debugging
      setError('Upload failed. Check console for details.');
      onInsights({ insights: '', financialData: {} });  // Reset data on error
    } finally {
      setLoading(false);  // Stop loading
    }
  };

  return (
    <div>
      <h2>Upload Financial Data</h2>
      <input 
        type="file" 
        accept=".csv,.xlsx,.pdf" 
        onChange={(e) => setFile(e.target.files[0])} 
        style={{ margin: '10px 0' }}  // Inline style for attractiveness
      />
      <button 
        onClick={handleUpload} 
        disabled={loading}  // Disable during loading
        style={{ 
          marginTop: '15px', 
          padding: '12px 25px', 
          background: loading ? '#ccc' : 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)', 
          color: 'white', 
          border: 'none', 
          borderRadius: '25px', 
          cursor: loading ? 'not-allowed' : 'pointer', 
          fontSize: '1rem', 
          fontWeight: '600', 
          transition: 'all 0.3s ease' 
        }}
      >
        {loading ? 'Uploading...' : 'Upload'}
      </button>
      {error && <p style={{ color: '#dc3545', marginTop: '15px' }}>{error}</p>}  {/* Error in red */}
    </div>
  );
}

export default Upload;