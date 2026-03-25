import React from 'react';

function DemandGauge({ score }) {
  const percentage = (score / 10) * 100;
  const color =
    score >= 7 ? 'var(--color-success)' :
    score >= 4 ? 'var(--color-warning)' :
    'var(--color-danger)';
  const label = score >= 7 ? 'High' : score >= 4 ? 'Medium' : 'Low';

  return (
    <div className="card gauge-card">
      <h3>Market Demand</h3>
      <div className="gauge">
        <div className="gauge-track">
          <div
            className="gauge-fill"
            style={{ width: `${percentage}%`, backgroundColor: color }}
          />
        </div>
        <div className="gauge-info">
          <span className="gauge-score" style={{ color }}>{score}/10</span>
          <span className="gauge-label">{label} demand</span>
        </div>
      </div>
    </div>
  );
}

export default DemandGauge;
