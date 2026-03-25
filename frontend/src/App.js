import React, { useState } from 'react';
import { Routes, Route, useNavigate } from 'react-router-dom';
import Header from './components/Header';
import AnalyzeForm from './components/AnalyzeForm';
import ResultsDashboard from './components/ResultsDashboard';
import HistoryPage from './components/HistoryPage';
import { analyzeJob } from './api';
import { useApi } from './hooks/useApi';
import { useTheme } from './context/ThemeContext';
import './App.css';

function HomePage() {
  const navigate = useNavigate();
  const { data: result, loading, error, execute } = useApi(analyzeJob);
  const [submitted, setSubmitted] = useState(false);

  const handleAnalyze = async (text) => {
    setSubmitted(true);
    try {
      await execute(text);
    } catch {
      // error is captured in hook
    }
  };

  return (
    <div className="page">
      <AnalyzeForm onSubmit={handleAnalyze} loading={loading} />
      {error && <div className="error-banner">{error}</div>}
      {submitted && result && <ResultsDashboard result={result} />}
    </div>
  );
}

function App() {
  const { theme } = useTheme();

  return (
    <div className={`app ${theme}`}>
      <Header />
      <main className="main-content">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/history" element={<HistoryPage />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;
