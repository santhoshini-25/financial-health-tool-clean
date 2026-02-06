import React, { useState } from 'react';
import axios from 'axios';

function Upload({ onInsights }) {
  const [file, setFile] = useState(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) {
      setError('Please select a file first.');
      return;
    }

    setLoading(true);
    setError('');

    const formData = new FormData();
    formData.append('file', file);
    formData.append('industry', 'Manufacturing');

    try {
      // ✅ Remove trailing slash if present
      const BASE_URL =
        (process.env.REACT_APP_API_URL || 'http://127.0.0.1:8000').replace(/\/$/, '');

      const response = await axios.post(
        `${BASE_URL}/upload`,
        formData
      );

      onInsights({
        insights: response.data.insights,
        financialData: response.data.data || {}
      });
    } catch (err) {
      console.error('Upload error:', err);
      setError('Upload failed. Please try again.');
      onInsights({ insights: '', financialData: {} });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Upload Financial Data</h2>

      <input
        type="file"
        accept=".csv,.xlsx,.pdf"
        onChange={(e) => setFile(e.target.files[0])}
        style={{ margin: '10px 0' }}
      />

      <button
        onClick={handleUpload}
        disabled={loading}
        style={{
          marginTop: '15px',
          padding: '12px 25px',
          background: loading
            ? '#ccc'
            : 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
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

      {error && (
        <p style={{ color: '#dc3545', marginTop: '15px' }}>
          {error}
        </p>
      )}
    </div>
  );
}

export default Upload;
