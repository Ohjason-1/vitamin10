import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [quote, setQuote] = useState("Do not watch the clock. Do what it does. Keep going.");
  const [loading, setLoading] = useState(false);

  const fetchQuote = async () => {
    setLoading(true);
    try {
      const response = await fetch('http://127.0.0.1:5000/api/quote');
      const data = await response.json();
      setQuote(data.quote);
    } catch (error) {
      console.error('Error fetching quote:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Quote of the Day</h1>
        <div className="quote-container">
          <p>{quote}</p>
        </div>
        <button onClick={fetchQuote} disabled={loading}>
          {loading ? 'Loading...' : 'Get Quote'}
        </button>
      </header>
    </div>
  );
}

export default App;