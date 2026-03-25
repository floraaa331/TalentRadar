import React, { useState } from 'react';
import Loading from './Loading';

function AnalyzeForm({ onSubmit, loading }) {
  const [text, setText] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (text.trim().length >= 20) {
      onSubmit(text.trim());
    }
  };

  return (
    <section className="card analyze-card">
      <h2>Analyze Job Description</h2>
      <p className="subtitle">Paste a job description to extract skills, seniority, salary estimates, and market demand.</p>
      <form onSubmit={handleSubmit}>
        <textarea
          className="textarea"
          rows={8}
          placeholder="Paste job description here (minimum 20 characters)..."
          value={text}
          onChange={(e) => setText(e.target.value)}
          disabled={loading}
        />
        <div className="form-footer">
          <span className="char-count">{text.length} characters</span>
          <button
            type="submit"
            className="btn btn-primary"
            disabled={loading || text.trim().length < 20}
          >
            {loading ? <Loading size="small" /> : 'Analyze'}
          </button>
        </div>
      </form>
    </section>
  );
}

export default AnalyzeForm;
